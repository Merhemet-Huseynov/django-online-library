from django.contrib import admin
from ..models import BookReview
from django.db.models import QuerySet
from typing import Optional


@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    """
    Admin configuration class for managing the BookReview model.

    This class defines how the BookReview model will appear and how it will
    be managed within the Django admin interface.
    """
    list_display = (
        "book", 
        "user", 
        "rating", 
        "created_at", 
        "short_review"
    )
    search_fields = (
        "book__title", 
        "user__username", 
        "review"
    )
    list_filter = (
        "rating", 
        "created_at"
    )
    ordering = (
        "-created_at",
    )

    def short_review(self, obj: BookReview) -> str:
        """
        Displays a short excerpt of the review, returning the first 50 characters.

        Args:
            obj (BookReview): The BookReview model instance

        Returns:
            str: The first 50 characters of the review, or an empty string if no review
        """
        return obj.review[:50] if obj.review else "" 

    short_review.short_description = "Short Review"  

    fields = (
        "book", 
        "user", 
        "rating", 
        "review", 
        "created_at"
    )
    readonly_fields = (
        "created_at",
    ) 
