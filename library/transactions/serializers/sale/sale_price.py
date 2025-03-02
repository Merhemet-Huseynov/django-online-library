from rest_framework import serializers
from books.models.catalog import Book
from transactions.models.sale import SalePrice


class SalePriceSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all()
    )
    
    class Meta:
        model = SalePrice
        fields = [
            "id", 
            "book", 
            "price"
        ]
