from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import timedelta
from django.db import models
from ..catalog.book import Book


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
        editable=False
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

    def save(self, *args, **kwargs):
        """
        Automatically sets rental_end_date, rental_price, 
        checks book availability.
        """
        if not self.pk and self.book.available_count <= 0:  
            raise ValueError(
                "The book is out of stock and cannot be rented."
            )
        
        if not self.pk: 
            self.book.available_count -= 1
            self.book.save()
        
       # Notify waiting users if the book is no longer available
        if self.book.available_count <= 0:
            users_waiting_for_book = RentalSchedule.objects.filter(
                book=self.book, status="pending"
            )
            for user_rental in users_waiting_for_book:
                OverdueNotification.objects.create(
                    user=user_rental.user,
                    book=self.book,
                    next_reminder_date=now().date() + timedelta(days=1) 
                )
        
        super().save(*args, **kwargs)

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

        # Only create RentalHistory when the book is actually returned and not already created
        if self.status == "returned" and not RentalHistory.objects.filter(
            user=self.user, book=self.book, rental_start_date=self.rental_start_date
        ).exists():
        
            RentalHistory.objects.create(
                user=self.user,
                book=self.book,
                rental_start_date=self.rental_start_date,
                rental_end_date=self.rental_end_date,
                rental_duration=self.rental_duration,
                rental_price=self.rental_price
            )