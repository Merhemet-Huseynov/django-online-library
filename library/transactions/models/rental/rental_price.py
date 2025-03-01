from django.db import models
from ..catalog.book import Book


class RentalPrice(models.Model):
    RENTAL_DURATIONS = [
        ("3_days", "3 Days"),
        ("1_week", "1 Week"),
        ("1_month", "1 Month"),
    ]

    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE, 
        related_name="rental_prices"
    )

    duration = models.CharField(
        max_length=10, 
        choices=RENTAL_DURATIONS
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )

    def __str__(self):
        return (
            f"Book: {self.book.title}\n"
            f"Duration: {self.get_duration_display()}\n"
            f"Price: {self.price} AZN"
        )
