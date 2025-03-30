from django.db import models
from django.contrib.auth import get_user_model
from books.models.catalog import Book

User = get_user_model()


class Payment(models.Model):
    """
    Model representing a payment transaction for purchasing a book.
    """

    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"

    PAYMENT_STATUS_CHOICES = [
        (PENDING, "Pending"),
        (COMPLETED, "Completed"),
        (FAILED, "Failed"),
        (REFUNDED, "Refunded"),
    ]

    CARD = "card"
    PAYPAL = "paypal"
    BALANCE = "balance"

    PAYMENT_METHOD_CHOICES = [
        (CARD, "Credit/Debit Card"),
        (PAYPAL, "PayPal"),
        (BALANCE, "Account Balance"),
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
    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHOD_CHOICES,
        help_text="The method used for the payment."
    )
    provider = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Payment gateway provider (e.g., Stripe, PayPal)."
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
    is_refunded = models.BooleanField(
        default=False,
        help_text="Indicates if the payment was refunded."
    )
    metadata = models.JSONField(
        blank=True, 
        null=True,
        help_text="Additional data from the payment gateway."
    )

    def __str__(self):
        return f"Payment of {self.amount} for {self.book.title} by {self.user.username}"
