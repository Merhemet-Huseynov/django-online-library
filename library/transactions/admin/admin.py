from django.contrib import admin
from ..models import (
    PurchaseHistory,
    RentalHistory,
)

# Register your models here.
admin.site.register(PurchaseHistory)
admin.site.register(RentalHistory)
