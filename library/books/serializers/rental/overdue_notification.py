from rest_framework import serializers
from django.contrib.auth.models import User
from models import Book, OverdueNotification

class OverdueNotificationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all()
    )

    class Meta:
        model = OverdueNotification
        fields = [
            "id", 
            "user", 
            "book", 
            "notification_sent_date", 
            "next_reminder_date"
        ]
