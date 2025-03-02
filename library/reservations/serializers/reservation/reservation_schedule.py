from rest_framework import serializers
from django.contrib.auth.models import User

from books.models.catalog import Book
from reservations.models.reservation import ReservationSchedule


class ReservationScheduleSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all()
    )

    class Meta:
        model = ReservationSchedule
        fields = [
            "id", 
            "user", 
            "book",
            "reservation_start_date", 
            "reservation_end_date", 
            "status"
        ]
