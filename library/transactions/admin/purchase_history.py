from django.contrib import admin
from ..models import PurchaseHistory


@admin.register(PurchaseHistory)
class PurchaseHistoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing the PurchaseHistory model in Django admin panel.
    """

    # Fields displayed in the admin panel
    list_display = (
        "id", 
        "user", 
        "book", 
        "purchase_date", 
        "sale_price",
        "user_name", 
        "book_title",  
    )

    # Fields used for search functionality
    search_fields = (
        "user__username",  
        "book__title",     
    )
 
    list_filter = ("purchase_date", "user", "book")
    ordering = ("-purchase_date",)

    def get_readonly_fields(self, request, obj=None):
        """
        Makes certain fields read-only in the admin panel.
        If the object is being edited, the user, book, and purchase date fields will be read-only.
        """
        if obj:
            return ("user", "book", "purchase_date")
        return super().get_readonly_fields(request, obj)

    def user_name(self, obj):
        """
        Returns the username of the user.
        """
        return obj.user.username
    user_name.admin_order_field = "user"  
    user_name.short_description = "User Name"

    def book_title(self, obj):
        """
        Returns the title of the book.
        """
        return obj.book.title
    book_title.admin_order_field = "book"
    book_title.short_description = "Book Title"
