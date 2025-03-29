from django.contrib import admin
from ..models import UserBookView


@admin.register(UserBookView)
class UserBookViewAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the UserBookView model.

    Features:
    - `list_display`: Specifies the fields displayed in the admin list view ("user", "book", "viewed_on").
    - `list_filter`: Enables filtering options by user and viewed date.
    - `search_fields`: Allows searching by username and book title.
    - `ordering`: Orders the records by viewed date in descending order.
    - `date_hierarchy`: Enables hierarchical navigation based on the viewed date.
    - `readonly_fields`: Makes the `viewed_on` field read-only to prevent modifications.
    """
    list_display = ("user", "book", "viewed_on") 
    list_filter = ("user", "viewed_on")  
    search_fields = ("user__username", "book__title") 
    ordering = ("-viewed_on",)  
    date_hierarchy = "viewed_on" 
    readonly_fields = ("viewed_on",)
