from django.db import models
from books.models import Book


class SalePrice(models.Model):
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):
        """
        Saves the sale price for the book. Deletes previous sale prices 
        for the same book before saving the new one.
        """
        if self.price:
            SalePrice.objects.filter(book=self.book).delete()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the sale price for the book.
        """
        return f"Sale price for {self.book.title}"
