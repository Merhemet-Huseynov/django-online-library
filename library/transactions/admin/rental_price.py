from django.contrib import admin
from ..models import RentalPrice
from books.models.catalog import Book


@admin.register(RentalPrice)
class RentalPriceAdmin(admin.ModelAdmin):
    """
    Admin configuration for the RentalPrice model. Customizes how the RentalPrice 
    objects are displayed and managed in the Django admin interface.

    Attributes:
        list_display (tuple): Defines the fields to be displayed in the list view.
        search_fields (tuple): Defines the fields to be searched in the admin search bar.
        list_filter (tuple): Defines the filters available on the right sidebar.
        ordering (tuple): Defines the default ordering of the RentalPrice objects in the list view.
        readonly_fields (tuple): Defines fields that are read-only in the admin form.
        fieldsets (tuple): Defines the layout and organization of fields in the admin form.

    Methods:
        get_duration_display(obj): Returns a formatted string displaying the rental duration and prices.
        save_model(request, obj, form, change): Customizes the saving of a RentalPrice instance.
    """
    
    list_display = ("book", "get_duration_display", "price_3_days", "price_1_week", "price_1_month")  
    search_fields = ("book__title",)  
    list_filter = ("book", "duration")  
    ordering = ("book",) 
    readonly_fields = ("get_duration_display",)
    fieldsets = (
        (None, {
            "fields": ("book", "duration", "price_3_days", "price_1_week", "price_1_month")
        }),
        ("Advanced options", {
            "classes": ("collapse",),
            "fields": ("get_duration_display",),
        }),
    )

    def get_duration_display(self, obj):
        """
        Returns a formatted string displaying the rental duration and corresponding prices.

        The method loops through the `duration` field of the RentalPrice object and 
        retrieves the corresponding price for each duration, then returns a string 
        that lists the duration and its associated price in AZN.

        Args:
            obj (RentalPrice): The RentalPrice instance being displayed in the admin.

        Returns:
            str: A formatted string of durations and their associated prices.
        """
        prices = []
        for duration in obj.duration:
            price = getattr(obj, f"price_{duration}", None)
            if price:
                prices.append(f"{dict(obj.RENTAL_DURATIONS).get(duration)}: {price} AZN")
        return ", ".join(prices)
    
    get_duration_display.short_description = "Duration (Price)"
    
    def save_model(self, request, obj, form, change):
        """
        Customizes the saving of a RentalPrice instance in the admin interface.

        This method is called when a RentalPrice instance is saved in the admin panel.
        The method ensures the standard saving process is followed while enabling any custom 
        actions if needed.

        Args:
            request (HttpRequest): The HTTP request object.
            obj (RentalPrice): The RentalPrice instance being saved.
            form (ModelForm): The form used to save the model.
            change (bool): Boolean indicating whether the object is being changed or created.
        """
        super().save_model(request, obj, form, change)
