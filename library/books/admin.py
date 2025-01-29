from django.contrib import admin
from .models import (
    Book,
    Category,
    Author,
    RentalSchedule,
    OverdueNotification,
    EventSchedule,
    ReservationSchedule
)

# Register your models here.
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(RentalSchedule)
admin.site.register(OverdueNotification)
admin.site.register(EventSchedule)
admin.site.register(ReservationSchedule)