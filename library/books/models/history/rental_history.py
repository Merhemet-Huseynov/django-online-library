from django.db import models
from ..catalog.book import Book
from django.contrib.auth.models import User

class RentalHistory(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="rental_history"
    )

    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE, 
        related_name="rental_history"
    )

    rental_start_date = models.DateField()
    rental_end_date = models.DateField()
    rental_duration = models.CharField(
        max_length=10, 
        choices=RentalSchedule.RENTAL_DURATIONS
    )
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return (
            f"Rental Details:\n"
            f"📌 User: {self.user.username}\n"
            f"📖 Book: {self.book.title}\n"
            f"📅 Rental Period: {self.rental_start_date} ➝ {self.rental_end_date}"
        )

    def save(self, *args, **kwargs):
        """Automatically creates RentalHistory after return."""
        super().save(*args, **kwargs)
        
        if self.status == "returned":
            rental_history_exists = RentalHistory.objects.filter(
                user=self.user, 
                book=self.book, 
                rental_start_date=self.rental_start_date
            ).exists()
            
            if not rental_history_exists:
                RentalHistory.objects.create(
                    user=self.user,
                    book=self.book,
                    rental_start_date=self.rental_start_date,
                    rental_end_date=self.rental_end_date,
                    rental_duration=self.rental_duration,
                    rental_price=self.rental_price
                )
