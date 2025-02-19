from django.db import models
from django.utils.timezone import now
from accounts.models.verification.daily_message_limit import DailyMessageLimit  


class DailyMessage(models.Model):
    email = models.EmailField()
    message_sent_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        indexes = [models.Index(fields=["email"])]

    def __str__(self):
        return f"Message sent to {self.email} at {self.message_sent_at}"

    @staticmethod
    def format_remaining_time(seconds):
        """Formats the remaining time into hours, minutes, and seconds."""
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours}:{minutes}:{seconds}"

    @classmethod
    def get_limit_info(cls):
        """Retrieves the daily message limit settings."""
        limit_obj, _ = DailyMessageLimit.objects.get_or_create(id=1)
        return limit_obj

    @classmethod
    def clear_old_messages(cls, email, reset_time):
        """Deletes old messages if the reset time has passed."""
        first_message = cls.objects.filter(
            email=email).order_by("message_sent_at").first()

        if first_message and (now() - first_message.message_sent_at >= reset_time):
            cls.objects.filter(email=email).delete()

    @classmethod
    def check_daily_limit(cls, email, limit, reset_time):
        """Checks if the user has reached the daily message limit."""
        today_messages_count = cls.objects.filter(
            email=email, message_sent_at__date=now().date()
        ).count()

        if today_messages_count >= limit:
            first_message_today = cls.objects.filter(
                email=email, 
                message_sent_at__date=now().date()
            ).order_by("message_sent_at").first()

            if first_message_today:
                remaining_time = (first_message_today.message_sent_at + reset_time) - now()
                seconds_remaining = max(int(remaining_time.total_seconds()), 0)
                return (
                    "You have reached your daily message limit. "
                    f"Please try again in {cls.format_remaining_time(seconds_remaining)} minutes."
                )

            return "You have reached your daily verification code limit, please try again later."

        return None

    @classmethod
    def check_expiration_time(cls, last_message, expiration_time):
        """Checks if the last message was sent within the expiration time."""
        if last_message:
            time_diff = now() - last_message.message_sent_at
            
            if time_diff < expiration_time:
                seconds_remaining = (expiration_time - time_diff).seconds
                return f"Please try again in  {cls.format_remaining_time(seconds_remaining)} to send a new message."

        return None

    @classmethod
    def send_message(cls, email):
        """Handles message sending logic while enforcing daily limits."""
        limit_obj = cls.get_limit_info()
        reset_time = limit_obj.reset_time

        cls.clear_old_messages(email, reset_time)

        limit_message = cls.check_daily_limit(
            email, 
            limit_obj.limit, 
            reset_time
        )
        if limit_message:
            return limit_message

        last_message = cls.objects.filter(
            email=email).order_by("-message_sent_at").first()

        expiration_message = cls.check_expiration_time(
            last_message, 
            limit_obj.expiration_time
        )

        if expiration_message:
            return expiration_message

        cls.objects.create(email=email)
        return "Message sent successfully!"
