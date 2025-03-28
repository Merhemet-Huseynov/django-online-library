from django.contrib import admin
from ..models import SalePrice
from books.models import Book


@admin.register(SalePrice)
class SalePriceAdmin(admin.ModelAdmin):
    """
    Configuration for the SalePrice model in the admin panel.
    Displays the book's price and creation date.
    """
    list_display = ("book", "price", "created_at")
    list_filter = ("book",)
    search_fields = ("book__title",)
    ordering = ("-created_at",)

    def book_title(self, obj):
        """
        Returns the title of the book.
        """
        return obj.book.title
    
    book_title.admin_order_field = "book__title"
    book_title.short_description = "Book Title"

    fieldsets = (
        (None, {
            "fields": ("book", "price")
        }),
    )
