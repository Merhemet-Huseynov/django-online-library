from django.contrib.auth.models import User
from books.models.catalog import Book
from notifications.models.overdue_notification import OverdueNotification


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
