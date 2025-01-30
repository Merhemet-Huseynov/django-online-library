from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from django.utils.timezone import now

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="books")
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, related_name="books")

    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=15, null=True, blank=True, unique=True)
    published_date = models.DateField()
    available = models.BooleanField(default=True)

    allow_rental = models.BooleanField(default=False)
    book_count = models.PositiveIntegerField(default=1)
    available_count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

    def average_rating(self):
        """Calculates the average rating of all reviews of the book."""
        reviews = self.reviews.all()
        if reviews.exists():
            total_rating = sum(review.rating for review in reviews)
            return total_rating / reviews.count()
        return 0


class RentalPrice(models.Model):
    RENTAL_DURATIONS = [
        ("3_days", "3 Days"),
        ("1_week", "1 Week"),
        ("1_month", "1 Month"),
    ]

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="rental_prices")
    duration = models.CharField(max_length=10, choices=RENTAL_DURATIONS)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.book.title} - {self.get_duration_display()} - {self.price} AZN"


class RentalSchedule(models.Model):
    RENTAL_DURATIONS = [
        ("3_days", "3 Days"),
        ("1_week", "1 Week"),
        ("1_month", "1 Month"),
    ]

    RENTAL_STATUS = [
        ("pending", "Pending"),
        ("active", "Active"),
        ("overdue", "Overdue"),
        ("returned", "Returned"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rentals")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="rentals")
    rental_start_date = models.DateField(auto_now_add=True)
    rental_end_date = models.DateField(editable=False)
    rental_duration = models.CharField(max_length=10, choices=RENTAL_DURATIONS, default="3_days")
    rental_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    returned = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=RENTAL_STATUS, default="pending")

    def save(self, *args, **kwargs):
        """Automatically sets rental_end_date, rental_price, checks book availability."""
        if not self.pk and self.book.available_count <= 0:  # Yeni obyekt yaradılarkən yoxla
            raise ValueError("The book is out of stock and cannot be rented.")

        if not self.pk:  # Yalnız yeni obyekt yaradılarkən azalmalıdır
            self.book.available_count -= 1
            self.book.save()

        duration_mapping = {
            "3_days": timedelta(days=3),
            "1_week": timedelta(weeks=1),
            "1_month": relativedelta(months=1),
        }
        self.rental_end_date = self.rental_start_date + duration_mapping.get(self.rental_duration, timedelta(days=3))

        # Gets the rental price of the book from the RentalPrice model
        rental_price_obj = RentalPrice.objects.filter(book=self.book, duration=self.rental_duration).first()
        if rental_price_obj:
            self.rental_price = rental_price_obj.price

        super().save(*args, **kwargs)

        # RentalHistory avtomatik yaradır
        if self.status == "returned" and not RentalHistory.objects.filter(user=self.user, book=self.book, rental_start_date=self.rental_start_date).exists():
            RentalHistory.objects.create(
                user=self.user,
                book=self.book,
                rental_start_date=self.rental_start_date,
                rental_end_date=self.rental_end_date,
                rental_duration=self.rental_duration,
                rental_price=self.rental_price
            )

    def return_book(self):
        """Method to return the book and update the available count, including overdue fine calculation."""
        if self.returned:
            raise ValueError("The book has already been returned.")

        self.returned = True
        self.book.available_count += 1
        self.book.save()

        # Overdue calculation
        today = now().date()
        overdue_days = max((today - self.rental_end_date).days, 0)  

        fine_amount = 0
        if overdue_days > 0:
            fine_amount = overdue_days * 1  

            OverdueFine.objects.create(
                rental=self,
                overdue_days=overdue_days,
                fine_amount=fine_amount
            )

        self.save()

    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({self.get_rental_duration_display()})"


class OverdueNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="notifications")
    notification_sent_date = models.DateField(auto_now_add=True)
    next_reminder_date = models.DateField()

    def __str__(self):
        return f"Overdue: {self.book.title} for {self.user.username}"


class OverdueFine(models.Model):
    rental = models.OneToOneField(RentalSchedule, on_delete=models.CASCADE, related_name="overdue_fine")
    overdue_days = models.PositiveIntegerField(default=0)
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Overdue Fine for {self.rental.book.title} ({self.overdue_days} days) - Fine: {self.fine_amount} AZN"


class SalePrice(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="sale_prices")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.book.title} - {self.price} AZN"


class SaleTransaction(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("canceled", "Canceled"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sales")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="sales")
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")

    def save(self, *args, **kwargs):
        """Automatically determines the selling price of the book."""
        if not self.sale_price:
            sale_price_obj = SalePrice.objects.filter(book=self.book).first()
            if sale_price_obj:
                self.sale_price = sale_price_obj.price

        super().save(*args, **kwargs)

        # PurchaseHistory avtomatik yaradır
        if self.status == "completed" and not PurchaseHistory.objects.filter(user=self.user, book=self.book, purchase_date=self.sale_date).exists():
            PurchaseHistory.objects.create(
                user=self.user,
                book=self.book,
                purchase_date=self.sale_date,
                sale_price=self.sale_price
            )

    def __str__(self):
        return f"Sale: {self.book.title} - {self.user.username} - {self.sale_price} AZN"


class EventSchedule(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ReservationSchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reservations")
    reservation_start_date = models.DateTimeField(auto_now_add=True)
    reservation_end_date = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=[("pending", "Pending"), ("confirmed", "Confirmed"), ("canceled", "Canceled")],
        default="pending",
    )

    def save(self, *args, **kwargs):
        """Checks availability before reservation and updates available_count."""
        if self.status == "confirmed" and self.book.available_count <= 0:
            raise ValueError("The book is out of stock and cannot be reserved.")

        if self.status == "confirmed" and not self.pk:  
            self.book.available_count -= 1
            self.book.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reservation: {self.book.title} by {self.user.username}"


class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="book_reviews")
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)]) 
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.book.title} - Rating: {self.rating}"


class RentalHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rental_history")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="rental_history")
    rental_start_date = models.DateField()
    rental_end_date = models.DateField()
    rental_duration = models.CharField(max_length=10, choices=RentalSchedule.RENTAL_DURATIONS)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Rental by {self.user.username} for {self.book.title} from {self.rental_start_date} to {self.rental_end_date}"


class PurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="purchase_history")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="purchase_history")
    purchase_date = models.DateField(auto_now_add=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Purchase by {self.user.username} for {self.book.title} on {self.purchase_date}"


class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="preferences")
    favorite_categories = models.ManyToManyField("Category", related_name="preferred_by", blank=True)
    favorite_authors = models.ManyToManyField("Author", related_name="preferred_by", blank=True)

    def __str__(self):
        return f"Preferences for {self.user.username}"


class BookRecommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recommendations")
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="recommendations")
    recommended_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Recommendation for {self.user.username} - {self.book.title}"

def generate_book_recommendations(user):
    # We find the categories the user is interested in
    preferences = user.preferences
    preferred_categories = preferences.favorite_categories.all()
    preferred_authors = preferences.favorite_authors.all()

    # User"s most rated books
    top_rated_books = Book.objects.filter(reviews__user=user).annotate(avg_rating=models.Avg("reviews__rating")).order_by("-avg_rating")[:5]

    # Popular books
    popular_books = Book.objects.all().order_by("-rental_count")[:5]  # rental_count özəlliyini əlavə et

    # Similar authors
    similar_author_books = Book.objects.filter(author__in=preferred_authors).exclude(id__in=[book.id for book in top_rated_books])

    # Combining recommended books
    recommended_books = set(top_rated_books) | set(popular_books) | set(similar_author_books)
  
    # Removing rented books
    rented_books = RentalSchedule.objects.filter(user=user, returned=False).values_list("book", flat=True)
    recommended_books = [book for book in recommended_books if book.id not in rented_books]

    # Creating a recommendation list
    for book in recommended_books:
        BookRecommendation.objects.create(user=user, book=book)

    return recommended_books