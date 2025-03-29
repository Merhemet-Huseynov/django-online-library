from django.db import models
from django.db.models import Count

from books.models.catalog import Book
from transactions.models.rental import RentalSchedule
from transactions.models.history import PurchaseHistory
from books.models.review import BookRecommendation


class UserPreferences(models.Model):
    """
    Stores user preferences, including favorite categories and authors.
    Provides methods to generate personalized book recommendations.
    """

    user = models.OneToOneField(
        "auth.User", 
        on_delete=models.CASCADE,
        related_name="preferences"
    )
    favorite_categories = models.ManyToManyField(
        "books.Category",  
        related_name="preferred_by", 
        blank=True
    )
    favorite_authors = models.ManyToManyField(
        "books.Author",
        related_name="preferred_by", 
        blank=True
    )

    def __str__(self):
        """Returns a string representation of the user's preferences."""
        return f"Preferences for {self.user.username}"

    def get_top_rated_books(self, limit=5):
        """
        Returns the user's highest-rated books based on review ratings.

        Args:
            limit (int): The maximum number of books to return.

        Returns:
            QuerySet: A queryset of the highest-rated books.
        """
        return (
            Book.objects.filter(reviews__user=self.user)
            .annotate(avg_rating=models.Avg("reviews__rating"))
            .order_by("-avg_rating")[:limit]
        )

    def get_popular_books(self, limit=5):
        """
        Returns the most rented books across all users.

        Args:
            limit (int): The maximum number of books to return.

        Returns:
            QuerySet: A queryset of the most rented books.
        """
        return Book.objects.annotate(rental_count=Count("rentals")).order_by("-rental_count")[:limit]

    def get_books_by_favorite_authors(self, exclude_books):
        """
        Returns books written by the user's favorite authors,
        excluding books the user has already rated.

        Args:
            exclude_books (list): A list of book IDs to exclude.

        Returns:
            QuerySet: A queryset of books from the user's favorite authors.
        """
        favorite_authors = self.user.preferences.favorite_authors.all()
        return Book.objects.filter(author__in=favorite_authors).exclude(id__in=exclude_books)

    def filter_unavailable_books(self, books):
        """
        Removes books that the user has already rented or purchased.

        Args:
            books (iterable): A list or queryset of books.

        Returns:
            list: A filtered list of books that the user has not rented or purchased.
        """
        rented_books = set(RentalSchedule.objects.filter(user=self.user, returned=False).values_list("book", flat=True))
        purchased_books = set(PurchaseHistory.objects.filter(user=self.user).values_list("book", flat=True))
        
        return [book for book in books if book.id not in rented_books and book.id not in purchased_books]

    def generate_book_recommendations(self):
        """
        Generates book recommendations based on the user's preferences and history.

        Returns:
            list: A list of recommended books for the user.
        """
        top_rated_books = self.get_top_rated_books()
        popular_books = self.get_popular_books()
        similar_author_books = self.get_books_by_favorite_authors(
            exclude_books=[book.id for book in top_rated_books]
        )

        # Merge recommendations and filter unavailable books
        recommended_books = set(top_rated_books) | set(popular_books) | set(similar_author_books)
        filtered_books = self.filter_unavailable_books(recommended_books)

        # Remove old recommendations and create new ones
        BookRecommendation.objects.filter(user=self.user).delete()
        BookRecommendation.objects.bulk_create(
            [BookRecommendation(user=self.user, book=book) for book in filtered_books]
        )

        return filtered_books
