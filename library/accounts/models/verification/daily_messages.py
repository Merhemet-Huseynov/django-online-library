from django.db import models
from django.utils.timezone import now


class DailyMessage(models.Model):
    email = models.EmailField()
    message_sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["email"]),
        ]

    def __str__(self):
        return f"Message sent to {self.email} at {self.message_sent_at}"

    @classmethod
    def send_message(cls, email):
        today_messages_count = cls.objects.filter(
            email=email, message_sent_at__date=now().date()
        ).count()

        if today_messages_count >= 3:
            return False 

        cls.objects.create(email=email)
        return True
