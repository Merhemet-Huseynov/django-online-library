from rest_framework import serializers
from notifications.models import OverdueNotification
from django.contrib.auth import get_user_model
from books.models.catalog import Book

User = get_user_model()


class OverdueNotificationSerializer(serializers.ModelSerializer):
    """
    Serializer for OverdueNotification model.

    This serializer handles the conversion between the OverdueNotification model 
    instances and JSON data. It includes fields for user, book, and notification_sent_date.
    """
    user = serializers.SlugRelatedField(
        slug_field="username", 
        queryset=User.objects.all()
    )
    book = serializers.SlugRelatedField(
        slug_field="title", 
        queryset=Book.objects.all()
    )

    class Meta:
        model = OverdueNotification
        fields = [
            "id",
            "user", 
            "book", 
            "notification_sent_date"
        ]
