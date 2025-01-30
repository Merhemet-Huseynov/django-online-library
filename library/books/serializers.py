from django.contrib.auth.models import User
from rest_framework import serializers

from .models import (
    Category,
    Author,
    Book,
    RentalSchedule,
    OverdueNotification,
    EventSchedule,
    ReservationSchedule,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id", 
            "name", 
            "description"
        ] 


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            "id", 
            "name", 
            "bio", 
            "birth_date"
        ]


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "category",
            "isbn",
            "published_date",
            "available",
            "sale_price",
            "rental_price_3_days",
            "rental_price_1_week",
            "rental_price_1_month",
            "allow_rental",
            "book_count"
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id", 
            "username", 
            "email", 
            "first_name", 
            "last_name", 
            "is_staff", 
            "is_active"
        ]


class RentalScheduleSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    
    # Include rental duration choices
    rental_duration = serializers.ChoiceField(choices=RentalSchedule.RENTAL_DURATIONS)
    rental_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    
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

    def create(self, validated_data):
        """Custom create method to automatically calculate rental_end_date and rental_price"""
        rental_schedule = super().create(validated_data)
        rental_schedule.save()
        return rental_schedule

    def update(self, instance, validated_data):
        """Custom update method to ensure rental_end_date and rental_price are calculated on update"""
        instance = super().update(instance, validated_data)
        instance.save() 
        return instance


class OverdueNotificationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = OverdueNotification
        fields = [
            "id", 
            "user", 
            "book", 
            "notification_sent_date", 
            "next_reminder_date"
        ]


class EventScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSchedule
        fields = [
            "id", 
            "name", 
            "description", 
            "start_time", 
            "end_time", 
            "location"
        ]


class ReservationScheduleSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

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