from django.db import models
from django.contrib.auth.models import User
from books.models.catalog import Book


class Payment(models.Model):
    """
    Model representing a payment transaction for purchasing a book.
    """
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"

    PAYMENT_STATUS_CHOICES = [
        (PENDING, "Pending"),
        (COMPLETED, "Completed"),
        (FAILED, "Failed"),
    ]

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        help_text="The user who made the payment."
    ) 
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        help_text="The book that is being purchased."
    )
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        help_text="The amount paid for the book."
    ) 
    status = models.CharField(
        max_length=10,
        choices=PAYMENT_STATUS_CHOICES,
        default=PENDING,
        help_text="The status of the payment."
    ) 
    payment_date = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when the payment was made."
    )
    transaction_id = models.CharField(
        max_length=255, 
        blank=True, 
        null=True,
        help_text="The unique transaction ID provided by the payment gateway."
    )

    def __str__(self):
        return f"Payment of {self.amount} for {self.book.title} by {self.user.username}"
