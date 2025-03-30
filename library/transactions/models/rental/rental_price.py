from django.db import models
from books.models.catalog import Book
from typing import List


class RentalPrice(models.Model):
    """
    Model to store rental prices for books based on different durations.

    Attributes:
        book (ForeignKey): The book associated with the rental price.
        duration (JSONField): A list of rental durations (e.g., 3 days, 1 week, 1 month).
        price_3_days (DecimalField): Price for a 3-day rental.
        price_1_week (DecimalField): Price for a 1-week rental.
        price_1_month (DecimalField): Price for a 1-month rental.
    """
    
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

    # Store durations as a list of strings
    duration = models.JSONField(
        blank=True,  
        default=list
    )

    # Prices for different durations
    price_3_days = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        blank=True, 
        null=True,
        help_text="Price for 3 days"
    )
    
    price_1_week = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        blank=True, 
        null=True,
        help_text="Price for 1 week"
    )

    price_1_month = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        blank=True, 
        null=True,
        help_text="Price for 1 month"
    )

    def __str__(self) -> str:
        """
        Return a string representation of the rental price details for a book.

        Includes the book title, the rental durations, and their corresponding prices.

        Returns:
            str: A human-readable string of the rental price details.
        """
        price_mapping = {
            "3_days": self.price_3_days,
            "1_week": self.price_1_week,
            "1_month": self.price_1_month
        }

        # Display prices for durations
        prices = [
            f"{dict(self.RENTAL_DURATIONS).get(duration)}: {price} AZN"
            for duration, price in price_mapping.items() if price
        ]

        return (
            f"Book: {self.book.title}\n"
            f"Duration(s): {', '.join(self.duration)}\n"
            f"Price(s): {', '.join(prices)}"
        )