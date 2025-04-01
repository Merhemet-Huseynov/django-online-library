from rest_framework import serializers
from django.contrib.auth.models import User

from books.models.catalog import Book
from transactions.models.history import PurchaseHistory


class PurchaseHistorySerializer(serializers.ModelSerializer):
    """
    Serializer for the PurchaseHistory model.
    Used to serialize purchase history data for API responses.
    """

    user_id = serializers.IntegerField(
        source="user.id", 
        read_only=True,
        help_text="Unique ID of the user."
    )
    user_name = serializers.CharField(
        source="user.username", 
        read_only=True,
        help_text="Username of the user."
    )
    book_id = serializers.IntegerField(
        source="book.id", 
        read_only=True,
        help_text="Unique ID of the purchased book."
    )
    book_title = serializers.CharField(
        source="book.title", 
        read_only=True,
        help_text="Title of the purchased book."
    )
    purchase_date = serializers.DateField(
        format="%Y-%m-%d",
        help_text="Purchase date (formatted as YYYY-MM-DD)."
    )
    sale_price = serializers.DecimalField(
        max_digits=10, 
        decimal_places=2,
        help_text="Sale price of the book."
    )

    class Meta:
        model = PurchaseHistory
        fields = [
            "id",
            "user_id", 
            "user_name", 
            "book_id", 
            "book_title", 
            "purchase_date", 
            "sale_price"
        ]
