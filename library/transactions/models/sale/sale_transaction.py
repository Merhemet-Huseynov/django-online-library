from django.db import models, transaction
from django.contrib.auth import get_user_model

from books.models.catalog import Book
from transactions.models.history import PurchaseHistory
from .sale_price import SalePrice

User = get_user_model()


class SaleTransaction(models.Model):
    """
    Represents a sale transaction for a book by a user.
    Tracks the sale price, date, and status of the transaction, and logs it in the purchase history.

    Attributes:
        user (ForeignKey): The user making the purchase.
        book (ForeignKey): The book being purchased.
        sale_price (DecimalField): The price at which the book is sold.
        sale_date (DateField): The date when the sale is made.
        status (CharField): The current status of the sale transaction (pending, completed, canceled).
    """
    
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("canceled", "Canceled"),
    ]

    user: User = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="sales"
    )
    book: Book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE, 
        related_name="sales"
    )
    sale_price: models.DecimalField = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )
    sale_date: models.DateField = models.DateField(
        auto_now_add=True
    )
    status: models.CharField = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default="pending"
    )

    def save(self, *args, **kwargs) -> None:
        """
        Save the sale transaction, updating the sale price from the SalePrice model
        and logging the transaction in the PurchaseHistory.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Raises:
            ValueError: If the sale price is not found in the SalePrice model.
        """
        with transaction.atomic():
            sale_price_obj = SalePrice.objects.filter(book=self.book).first()

            if not sale_price_obj or sale_price_obj.price is None:
                raise ValueError("Sale price is not available, the transaction has been stopped.")

            self.sale_price = sale_price_obj.price  
            super().save(*args, **kwargs)

            # Each sale will be logged in the PurchaseHistory
            PurchaseHistory.objects.create(
                user=self.user,
                book=self.book,
                purchase_date=self.sale_date,
                sale_price=self.sale_price
            )

    def __str__(self) -> str:
        """
        Return a string representation of the SaleTransaction instance.

        Returns:
            str: A string describing the sale transaction with book title, user, and sale price.
        """
        return f"Sale: {self.book.title} - {self.user.username} - {self.sale_price} AZN"
