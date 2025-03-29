from django.contrib import admin
from ..models import BookRecommendation


@admin.register(BookRecommendation)
class BookRecommendationAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing the BookRecommendation model.

    Features:
    - list_display: Defines the fields displayed in the list view (user, book, recommended_on).
    - search_fields: Enables searching by user username and book title.
    - list_filter: Allows filtering by recommendation date.
    - readonly_fields: Makes the recommended_on field read-only.
    """

    list_display = ("user", "book", "recommended_on")
    search_fields = ("user__username", "book__title")
    list_filter = ("recommended_on",)  
    readonly_fields = ("recommended_on",)  

    def preview_recommendation(self, obj):
        """
        Returns a short preview of the book recommendation.

        Parameters:
        - obj (BookRecommendation): The recommendation instance.

        Returns:
        - str: A brief summary including the user and book details.
        """
        return f"Recommendation for {obj.user.username} - {obj.book.title}"  

    preview_recommendation.short_description = "Preview"
