from django.contrib import admin
from django.utils.html import format_html
from ..models import UserPreferences
from books.models import BookRecommendation


@admin.register(UserPreferences)
class UserPreferencesAdmin(admin.ModelAdmin):
    """Admin panel configuration for managing user preferences."""

    list_display = (
        "user",
        "favorite_categories_display",
        "favorite_authors_display",
        "top_rated_books_preview",
        "recommended_books_preview",
    )
    search_fields = ("user__username", "user__email")
    list_filter = ("favorite_categories", "favorite_authors")

    def favorite_categories_display(self, obj):
        """Display favorite categories in a more readable format."""
        return ", ".join([category.name for category in obj.favorite_categories.all()])
    
    favorite_categories_display.short_description = "Favorite Categories"

    def favorite_authors_display(self, obj):
        """Display favorite authors in a more readable format."""
        return ", ".join([author.name for author in obj.favorite_authors.all()])
    
    favorite_authors_display.short_description = "Favorite Authors"

    def top_rated_books_preview(self, obj):
        """Display the top-rated books for preview in the admin panel."""
        top_books = obj.get_top_rated_books(limit=3)
        return format_html(
            "<br>".join(
                [f"<a href='/admin/books/book/{book.id}/'>{book.title}</a>" for book in top_books]
            )
        )
    
    top_rated_books_preview.short_description = "Top Rated Books Preview"

    def recommended_books_preview(self, obj):
        """Display the generated book recommendations in the admin panel."""
        recommendations = obj.generate_book_recommendations()
        return format_html(
            "<br>".join(
                [f"<a href='/admin/books/book/{book.id}/'>{book.title}</a>" for book in recommendations]
            )
        )
    
    recommended_books_preview.short_description = "Recommended Books Preview"
