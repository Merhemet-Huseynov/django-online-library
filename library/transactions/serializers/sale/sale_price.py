from rest_framework import serializers
from transactions.models.sale import SalePrice


class SalePriceSerializer(serializers.ModelSerializer):
    """
    Serializer for converting SalePrice model instances to JSON format.
    Includes book title, price, and creation date (created_at).
    """
    
    book_title = serializers.CharField(
        source="book.title",  
        read_only=True
    )
    created_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", 
        read_only=True
    )

    class Meta:
        model = SalePrice
        fields = [
            "id", 
            "book", 
            "book_title", 
            "price", 
            "created_at"
        ]
        read_only_fields = [
            "id", 
            "created_at"
        ]
