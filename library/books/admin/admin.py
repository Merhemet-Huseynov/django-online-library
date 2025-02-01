from django.contrib import admin
from ..models import (
    Book,
    Category,
    Author,
    EventSchedule,
    PurchaseHistory,
    RentalHistory,
    OverdueFine,
    OverdueNotification,
    RentalPrice,
    RentalSchedule,
    ReservationSchedule,
    BookReview,
    SalePrice,
    SaleTransaction,
    BookRecommendation,
    UserPreferences
)

# Register your models here.
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(EventSchedule)
admin.site.register(PurchaseHistory)
admin.site.register(RentalHistory)
admin.site.register(OverdueFine)
admin.site.register(OverdueNotification)
admin.site.register(RentalPrice)
admin.site.register(RentalSchedule)
admin.site.register(ReservationSchedule)
admin.site.register(BookReview)
admin.site.register(SalePrice)
admin.site.register(SaleTransaction)
admin.site.register(BookRecommendation)
admin.site.register(UserPreferences)