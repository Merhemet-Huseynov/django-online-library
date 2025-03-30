from django.contrib import admin
from books.models.catalog import Book
from payments.models.payment import Payment
from ..models import RentalSchedule  


def get_rental_price_model():
    from ..models import RentalPrice  
    return RentalPrice


@admin.register(RentalSchedule)
class RentalScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "user", 
        "book", 
        "rental_start_date", 
        "rental_end_date", 
        "rental_duration", 
        "rental_price", 
        "status", 
        "returned"
    )
    search_fields = ("user__username", "book__title")
    list_filter = ("status", "rental_duration")
    actions = ["mark_as_returned", "mark_as_overdue"]

    def mark_as_returned(self, request, queryset):
        queryset.update(status="returned", returned=True)
    mark_as_returned.short_description = "Mark selected rentals as returned"

    def mark_as_overdue(self, request, queryset):
        queryset.update(status="overdue")
    mark_as_overdue.short_description = "Mark selected rentals as overdue"

    fieldsets = (
        (None, {
            "fields": (
                "user", 
                "book", 
                "rental_start_date", 
                "rental_duration", 
                "status", 
                "returned"
            )
        }),
    )

    readonly_fields = ("rental_start_date", "rental_end_date", "rental_price")

    def rental_price(self, obj):
        """
        Displays the rental price based on the selected rental duration.
        
        The price is fetched from the RentalPrice model based on the associated book.
        If the rental duration is 3 days, 1 week, or 1 month, the respective price 
        is returned. If no price is found for the selected duration, "N/A" is returned.

        :param obj: RentalSchedule instance
        :return: Rental price as a string (price or "N/A")
        """
        RentalPrice = get_rental_price_model()  
        rental_price_obj = RentalPrice.objects.filter(book=obj.book).first()
        if rental_price_obj:
            if obj.rental_duration == "3_days":
                return rental_price_obj.price_3_days
            elif obj.rental_duration == "1_week":
                return rental_price_obj.price_1_week
            elif obj.rental_duration == "1_month":
                return rental_price_obj.price_1_month
        return "N/A"

    rental_price.short_description = "Rental Price"
