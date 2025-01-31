from rest_framework import serializers
from models import Book, SalePrice

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
