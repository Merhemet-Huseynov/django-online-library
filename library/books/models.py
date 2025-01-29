from django.db import models
from django.contrib.auth.models import User

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
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name="books"
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name="books"
    )
    isbn = models.CharField(max_length=13, null=True, blank=True, unique=True)
    published_date = models.DateField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class RentalSchedule(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="rentals"
    )
    book = models.ForeignKey(
        "Book", 
        on_delete=models.CASCADE, 
        related_name="rentals"
    )
    rental_start_date = models.DateField(auto_now_add=True)
    rental_end_date = models.DateField()
    returned = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices=[
            ("active", "Active"),
            ("overdue", "Overdue"),
            ("returned", "Returned"),
            ("pending", "Pending"),
        ],
        default="active",
    )

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"


class OverdueNotification(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="notifications"
    )
    book = models.ForeignKey(
        "Book", 
        on_delete=models.CASCADE, 
        related_name="notifications"
    )
    notification_sent_date = models.DateField(auto_now_add=True)
    next_reminder_date = models.DateField()

    def __str__(self):
        return f"Overdue: {self.book.title} for {self.user.username}"


class EventSchedule(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ReservationSchedule(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="reservations"
    )
    book = models.ForeignKey(
        "Book", 
        on_delete=models.CASCADE, 
        related_name="reservations"
    )
    reservation_start_date = models.DateTimeField(auto_now_add=True)
    reservation_end_date = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("confirmed", "Confirmed"),
            ("canceled", "Canceled"),
        ],
        default="pending",
    )

    def __str__(self):
        return f"Reservation: {self.book.title} by {self.user.username}"