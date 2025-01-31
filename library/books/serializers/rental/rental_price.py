from rest_framework import serializers
from models import Book, RentalPrice

class RentalPriceSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all()
    )

    class Meta:
        model = RentalPrice
        fields = [
            "id",
            "book", 
            "duration", 
            "price"
        ]
