from django.db import models
from django.contrib.auth.models import User
from ..catalog.book import Book


class ReservationSchedule(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="reservations"
    )
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE, 
        related_name="reservations"
    )

    reservation_start_date = models.DateTimeField(
        auto_now_add=True
    )
    reservation_end_date = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"), 
            ("confirmed", "Confirmed"), 
            ("canceled", "Canceled")
        ],
        default="pending",
    )

    def save(self, *args, **kwargs):
        """Check book availability and prevent duplicate orders."""
        if self.status == "confirmed" and self.book.available_count <= 0:
            raise ValueError("The book is out of stock and cannot be reserved.")
        
        if self.status == "confirmed" and not self.pk:
            self.book.available_count -= 1
            self.book.save()

            # Notify waiting users if the book is no longer available
            if self.book.available_count <= 0:
                users_waiting_for_book = ReservationSchedule.objects.filter(
                    book=self.book, 
                    status="pending"
                )
                for user_reservation in users_waiting_for_book:
                    OverdueNotification.objects.create(
                        user=user_reservation.user,
                        book=self.book,
                        next_reminder_date=now().date() + timedelta(days=1) 
                    )

        super().save(*args, **kwargs)