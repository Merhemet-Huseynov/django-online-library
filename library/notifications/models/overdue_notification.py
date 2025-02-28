from django.db import models
from django.contrib.auth.models import User
from books.models.catalog import Book
from django.utils.timezone import now


class OverdueNotification(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="notifications"
    )
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE, 
        related_name="notifications"
    )
    
    notification_sent_date = models.DateField(
        auto_now_add=True
    )
    next_reminder_date = models.DateField()

    def __str__(self):
        return f"Overdue: {self.book.title} for {self.user.username}"