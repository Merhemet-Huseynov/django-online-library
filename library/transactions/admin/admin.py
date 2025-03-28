from django.contrib import admin
from ..models import (
    PurchaseHistory,
    RentalHistory,
    OverdueFine,
    RentalPrice,
    RentalSchedule,
    SaleTransaction,
)

# Register your models here.
admin.site.register(PurchaseHistory)
admin.site.register(RentalHistory)
admin.site.register(OverdueFine)
admin.site.register(RentalPrice)
admin.site.register(RentalSchedule)
admin.site.register(SaleTransaction)
