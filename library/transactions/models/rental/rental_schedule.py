from django.db import models
from datetime import timedelta
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from django.apps import apps

from books.models.catalog import Book
from payments.models.payment import Payment

User = get_user_model()


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

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="rentals"
    )
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE, 
        related_name="rentals"
    )

    rental_start_date = models.DateField(
        auto_now_add=True
    )
    rental_end_date = models.DateField(
        blank=True,
        null=True
    )
    rental_duration = models.CharField(
        max_length=10, 
        choices=RENTAL_DURATIONS, 
        default="3_days"
    )
    rental_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True
    )

    returned = models.BooleanField(
        default=False
    )
    status = models.CharField(
        max_length=20, 
        choices=RENTAL_STATUS, 
        default="pending"
    )

    def rent_book(self):
        """
        Process the book rental, ensuring availability and handling payments.

        Steps:
        1. Check book availability.
        2. Set the rental price.
        3. Process the payment.
        4. Update book availability and rental status.
        5. Calculate the rental end date.
        """
        RentalPrice = apps.get_model('transactions', 'RentalPrice')

        # Check if the book is available
        if self.book.available_count <= 0:
            raise ValueError("The book is currently not available for rent.")
        
        # Ensure rental price is set
        if not self.rental_price:
            rental_price_obj = RentalPrice.objects.filter(book=self.book).first()
            if rental_price_obj:
                self.rental_price = rental_price_obj.price
            else:
                raise ValueError("The rental price for the book is not set.")

        # Process payment
        payment = Payment.objects.create(
            user=self.user,
            book=self.book,
            amount=self.rental_price,
            status=Payment.PENDING,
            payment_method=Payment.BALANCE, 
        )
        
        # Simulate payment completion
        payment.status = Payment.COMPLETED
        payment.save()

        # Ensure payment was successful before proceeding
        if payment.status != Payment.COMPLETED:
            raise ValueError("Payment failed. Rental cannot be processed.")

        # Update rental status and book availability
        self.status = "active"
        self.book.available_count -= 1
        self.book.save()

        # Set rental end date
        if self.rental_duration == "3_days":
            self.rental_end_date = self.rental_start_date + timedelta(days=3)
        elif self.rental_duration == "1_week":
            self.rental_end_date = self.rental_start_date + timedelta(weeks=1)
        elif self.rental_duration == "1_month":
            self.rental_end_date = self.rental_start_date + timedelta(weeks=4)

        self.save()

        return f"Book \"{self.book.title}\" rented successfully. Rental period: {self.rental_start_date} ➝ {self.rental_end_date}"
