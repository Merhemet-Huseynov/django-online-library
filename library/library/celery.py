from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Django settings modulunu təyin et
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library.settings")

app = Celery("library")

# Django settings-dən Celery konfiqurasiyasını oxu
app.config_from_object("django.conf:settings", namespace="CELERY")

# Celery task-larını tapmaq üçün Django app-larını aşkar et
app.autodiscover_tasks()
