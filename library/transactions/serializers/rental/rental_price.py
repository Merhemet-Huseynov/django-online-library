from rest_framework import serializers

from transactions.models.rental import RentalPrice
from books.models.catalog import Book


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
