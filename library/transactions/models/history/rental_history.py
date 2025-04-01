from django.db import models
from books.models.catalog import Book
from transactions.models.rental import RentalSchedule
from django.contrib.auth.models import User


class RentalHistory(models.Model):
    """
    Model to store users' book rental history.
    """
    
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
    rental_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2 
    )

    def __str__(self):
        """
        String representation of the model instance.
        """
        return (
            f"Rental Details:\n"
            f"📌 User: {self.user.username}\n"
            f"📖 Book: {self.book.title}\n"
            f"📅 Rental Period: {self.rental_start_date} ➝ {self.rental_end_date}"
        )

    def save(self, *args, **kwargs):
        """
        Performs additional checks before saving the rental history.
        """
        super().save(*args, **kwargs)
