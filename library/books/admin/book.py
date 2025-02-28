from django.contrib import admin
from django.utils.html import format_html
from ..models import Book, Category, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Book objects.
    """
    # Fields displayed in the admin list view
    list_display = (
        "title",
        "author",
        "category",
        "isbn",
        "published_date",
        "condition",
        "book_format",
        "available_count",
        "allow_rental",
        "image_preview",
        "display_tags",
    )

    # Searchable fields
    search_fields = (
        "title",
        "isbn",
        "author__name",
        "category__name",
        "tags__name",
    )

    # Filtering options
    list_filter = (
        "book_format",
        "condition",
        "available",
        "allow_rental",
        "category",
        "tags",
    )

    # Read-only fields (cannot be edited)
    readonly_fields = ("added_date",)

    # Organizing fields into sections
    fieldsets = (
        (None, {
            "fields": (
                "title",
                "isbn",
                "author",
                "description",
                "published_date",
            )
        }),
        ("Book Details", {
            "fields": (
                "category",
                "condition",
                "book_format",
                "page_count",
                "edition",
                "publisher",
                "language",
                "shelf_location",
            )
        }),
        ("Physical and Digital Files", {
            "fields": (
                "image",
                "digital_file",
            )
        }),
        ("Availability", {
            "fields": (
                "tags",
                "allow_rental",
                "available",
                "book_count",
                "available_count",
            )
        }),
    )

    # Default ordering (latest books first)
    ordering = ("-published_date",)

    # Image preview in the list view
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="auto" style="border-radius: 5px;" />',
                obj.image.url,
            )
        return "No Image"
    
    image_preview.short_description = "Image Preview"

    # Display tags in the admin panel
    def display_tags(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())

    display_tags.short_description = "Tags"

    # 📌 Bulk actions (Mark books as available/unavailable)
    actions = ["make_available", "make_unavailable"]

    def make_available(self, request, queryset):
        queryset.update(available=True)
        self.message_user(request, "Selected books are now available.")
    
    def make_unavailable(self, request, queryset):
        queryset.update(available=False)
        self.message_user(request, "Selected books are now unavailable.")

    make_available.short_description = "Mark selected books as available"
    make_unavailable.short_description = "Mark selected books as unavailable"
