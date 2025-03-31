from celery.schedules import crontab
from celery import Celery
from transactions.tasks import calculate_all_fines

app = Celery("library")

app.conf.beat_schedule = {
    "calculate-overdue-fines-daily": {
        "task": "transactions.tasks.calculate_all_fines",
        "schedule": crontab(hour=0, minute=0),
    },
}
