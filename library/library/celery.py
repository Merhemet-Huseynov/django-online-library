from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Django settings modulu üçün default ayarını təyin et
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library.settings")

app = Celery("library")

# Django'nun settings.py-dəki Celery konfiqurasiyasını oxu
app.config_from_object("django.conf:settings", namespace="CELERY")

# Task-ları aşkar etmək üçün Django'nun app-larını tapın
app.autodiscover_tasks()
