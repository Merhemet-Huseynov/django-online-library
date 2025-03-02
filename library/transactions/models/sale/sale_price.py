from django.db import models
from books.models.catalog import Book


class SalePrice(models.Model):
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE, 
        related_name="sale_prices"
    )
    
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )

    def __str__(self):
        return f"{self.book.title} - {self.price} AZN"
