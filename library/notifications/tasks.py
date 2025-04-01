from celery import shared_task
from django.core.mail import send_mail
from django.utils.timezone import now, timedelta
from decouple import config
from django.apps import apps

@shared_task
def send_overdue_notification():
    RentalSchedule = apps.get_model("transactions", "RentalSchedule")
    OverdueNotification = apps.get_model("notifications", "OverdueNotification")
    sender_email = config("EMAIL_HOST_USER")  # Email göndəricisini configdən alırıq
    
    tomorrow = now().date() + timedelta(days=1)
    rentals = RentalSchedule.objects.filter(rental_end_date=tomorrow, status="active")

    for rental in rentals:
        notification, created = OverdueNotification.objects.get_or_create(
            user=rental.user,
            book=rental.book,
            defaults={"notification_sent_date": now().date()},
        )
        if not created:
            notification.notification_sent_date = now().date()
            notification.save()

        # Email göndər
        send_mail(
            subject="Overdue Book Reminder",
            message=f"Reminder: Your rental for '{rental.book.title}' expires tomorrow!",
            from_email=sender_email,  # Bu hissə düzəldildi
            recipient_list=[rental.user.email],  # Emaili düzəldirik
        )
