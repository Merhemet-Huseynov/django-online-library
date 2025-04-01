from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now, timedelta
from django.apps import apps
from notifications.tasks import send_overdue_notification

RentalSchedule = apps.get_model("transactions", "RentalSchedule")

@receiver(post_save, sender=RentalSchedule)
def trigger_overdue_notification(sender, instance, **kwargs):
    """
    Triggers an overdue notification task if the rental schedule is active 
    and its end date is one day ahead.
    """
    if instance.rental_end_date == now().date() + timedelta(days=1) and instance.status == "active":
        send_overdue_notification.delay()
