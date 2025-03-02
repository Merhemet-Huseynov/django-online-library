from django.db import models
from books.models.catalog import Book
from django.contrib.auth.models import User


class PurchaseHistory(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="purchase_history"
    )
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE, 
        related_name="purchase_history"
    )
    
    purchase_date = models.DateField(
        auto_now_add=True
    )
    sale_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )

    def __str__(self):
        return (
            f"Purchase Details:\n"
            f"- User: {self.user.username}\n"
            f"- Book: {self.book.title}\n"
            f"- Date: {self.purchase_date}"
        )
