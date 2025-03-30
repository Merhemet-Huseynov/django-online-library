from rest_framework import serializers
from transactions.models.rental import RentalPrice
from books.models.catalog import Book
from typing import Optional


class RentalPriceSerializer(serializers.ModelSerializer):
    """
    Serializer for the RentalPrice model.

    This serializer is responsible for transforming the RentalPrice model
    into a JSON representation. It includes fields for book-related data,
    displayable duration, and rental prices for different periods (3 days, 1 week, 1 month).
    """

    book: serializers.PrimaryKeyRelatedField = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all()
    )
    
    book_title: serializers.CharField = serializers.CharField(
        source="book.title", 
        read_only=True
    )
    
    duration_display: serializers.CharField = serializers.CharField(
        source="get_duration_display", 
        read_only=True
    )

    price_3_days: Optional[serializers.DecimalField] = serializers.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        required=False, 
        allow_null=True
    )

    price_1_week: Optional[serializers.DecimalField] = serializers.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        required=False, 
        allow_null=True
    )

    price_1_month: Optional[serializers.DecimalField] = serializers.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        required=False, 
        allow_null=True
    )

    class Meta:
        model = RentalPrice
        fields = [
            "id", 
            "book", 
            "book_title", 
            "duration", 
            "duration_display", 
            "price_3_days", 
            "price_1_week", 
            "price_1_month"
        ]