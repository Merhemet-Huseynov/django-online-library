from django.contrib import admin
from ..models import (
    PurchaseHistory,
    RentalHistory,
    OverdueFine,
)

# Register your models here.
admin.site.register(PurchaseHistory)
admin.site.register(RentalHistory)
admin.site.register(OverdueFine)
