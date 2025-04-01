from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now, timedelta
from books.models.catalog import Book
from django.apps import apps

User = get_user_model()


class OverdueNotification(models.Model):
    """
    Model for tracking overdue notifications sent to users for their rented books.

    Attributes:
        user (ForeignKey): The user who is notified.
        book (ForeignKey): The book that is overdue.
        notification_sent_date (DateField): The date when the notification was sent.
    """
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
    notification_sent_date = models.DateField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the OverdueNotification instance.

        Returns:
            str: A string indicating the overdue book and the user.
        """
        return f"Reminder: {self.book.title} for {self.user.username}"

    def send_notification(self):
        """
        Sends a notification to the user about the overdue book.

        This method currently prints a reminder message to the console.
        In the future, this could be extended to send an email or SMS notification.
        """
        print(f"Reminder: Your rental for {self.book.title} expires tomorrow, {self.user.username}!")

    @classmethod
    def check_and_send_reminders(cls):
        """
        Checks for rentals that are due tomorrow and sends reminders to users.

        This method dynamically loads the RentalSchedule model and checks for active rentals
        that are due the next day. It creates or updates overdue notifications for these rentals
        and sends the reminders.
        """
        tomorrow = now().date() + timedelta(days=1)
        RentalSchedule = apps.get_model("transactions", "RentalSchedule")
        rentals = RentalSchedule.objects.filter(rental_end_date=tomorrow, status="active")

        for rental in rentals:
            notification, created = cls.objects.get_or_create(
                user=rental.user,
                book=rental.book,
                defaults={"notification_sent_date": now().date()},
            )
            if not created:
                notification.notification_sent_date = now().date()
                notification.save()

            notification.send_notification()
