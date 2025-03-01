from django.contrib import admin
from ..models import EventSchedule, ReservationSchedule


# Register your models here.
admin.site.register(EventSchedule)
admin.site.register(ReservationSchedule)