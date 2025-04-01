from django.contrib import admin
from ..models import RentalHistory


@admin.register(RentalHistory)
class RentalHistoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for the RentalHistory model.
    Provides listing, filtering, and search functionalities.
    """

    list_display = (
        "id", 
        "user", 
        "book", 
        "rental_start_date", 
        "rental_end_date",
        "rental_duration",
        "rental_price",
    )

    search_fields = (
        "user__username",  
        "book__title",     
    )

    list_filter = ("rental_start_date", "rental_end_date", "user", "book")

    ordering = ("-rental_start_date",)

    def get_readonly_fields(self, request, obj=None):
        """
        Makes specific fields read-only when editing an existing record.
        """
        if obj:
            return ("user", "book", "rental_start_date")
        return super().get_readonly_fields(request, obj)
