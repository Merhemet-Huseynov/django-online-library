from django.db import models
from django.contrib.auth.models import User
from ..catalog.book import Book


class SaleTransaction(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("canceled", "Canceled"),
    ]

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="sales"
    )
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE, 
        related_name="sales"
    )

    sale_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )
    sale_date = models.DateField(
        auto_now_add=True
    )
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default="pending"
    )

    def save(self, *args, **kwargs):
        """Automatically determines the selling price of the book."""
        if not self.sale_price:
            sale_price_obj = SalePrice.objects.filter(
                book=self.book
            ).first()

            if sale_price_obj:
                self.sale_price = sale_price_obj.price

        super().save(*args, **kwargs)

        # PurchaseHistory automatically creates
        if self.status == "completed" and not PurchaseHistory.objects.filter(
            user=self.user, 
            book=self.book, 
            purchase_date=self.sale_date
        ).exists():

            PurchaseHistory.objects.create(
                user=self.user,
                book=self.book,
                purchase_date=self.sale_date,
                sale_price=self.sale_price
            )

    def __str__(self):
        return f"Sale: {self.book.title} - {self.user.username} - {self.sale_price} AZN"
