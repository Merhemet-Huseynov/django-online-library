from celery.schedules import crontab
from celery import Celery

from transactions.tasks import calculate_all_fines
from notifications.tasks import send_overdue_notification

app = Celery("library")

app.conf.beat_schedule = {
    "calculate-overdue-fines-daily": {
        "task": "transactions.tasks.calculate_all_fines",
        "schedule": crontab(hour=0, minute=0),
    },
    "send-overdue-notifications-every-day": {
        "task": "notifications.tasks.send_overdue_notification",
        "schedule": crontab(hour=0, minute=0), 
    },
}