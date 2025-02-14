from rest_framework import serializers 
from django.contrib.auth.models import User

from books.models.catalog import Book
from books.models.rental import RentalSchedule


class RentalScheduleSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all()
    )

    class Meta:
        model = RentalSchedule
        fields = [
            "id", 
            "user", 
            "book", 
            "rental_start_date", 
            "rental_end_date", 
            "rental_duration", 
            "rental_price", 
            "returned", 
            "status"
        ]
