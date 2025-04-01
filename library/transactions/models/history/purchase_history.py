from django.db import models
from books.models.catalog import Book
from django.contrib.auth.models import User


class PurchaseHistory(models.Model):
    """
    Model to store the purchase history of books bought by users.
    """

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="purchase_history",
        help_text="The user who purchased the book."
    )
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE, 
        related_name="purchase_history",
        help_text="The book that was purchased."
    )
    
    purchase_date = models.DateField(
        auto_now_add=True,
        help_text="The date of purchase. Automatically set."
    )
    sale_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        help_text="The sale price of the book."
    )

    def __str__(self):
        """
        String representation of the PurchaseHistory object.
        """
        return (
            f"Purchase Details:\n"
            f"- User: {self.user.username}\n"
            f"- Book: {self.book.title}\n"
            f"- Date: {self.purchase_date}"
        )
