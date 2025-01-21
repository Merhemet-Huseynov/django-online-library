from __future__ import absolute_import, unicode_literals
from celery import celery
import os

# Django settings modulu üçün default ayarını təyin edilir
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library.settings")

app = celery.library

# Django'nun settings.py-dəki Celery konfiqurasiyasını oxu
app.config_from_object("django.conf:settings", namespace="CELERY")

# Task-ları aşkar etmək üçün Django'nun app-larını tapın
app.autodiscover_tasks()

