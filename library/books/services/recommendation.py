from django.db import models
from django.db.models import Count
from models.catalog.book import Book
from transactions.models.rental.rental_schedule import RentalSchedule
from transactions.models.history.purchase_history import PurchaseHistory
from books.models.review import BookRecommendation


def get_top_rated_books(user, limit=5):
    """Returns the user's highest-rated books."""
    return (
        Book.objects.filter(reviews__user=user)
        .annotate(avg_rating=models.Avg("reviews__rating"))
        .order_by("-avg_rating")[:limit]
    )


def get_popular_books(limit=5):
    """Returns the most rented books."""
    return Book.objects.annotate(rental_count=Count("rentals")).order_by("-rental_count")[:limit]


def get_books_by_favorite_authors(user, exclude_books):
    """Returns books from the user's favorite authors, excluding already rated ones."""
    favorite_authors = user.preferences.favorite_authors.all()
    return Book.objects.filter(author__in=favorite_authors).exclude(id__in=exclude_books)


def filter_unavailable_books(user, books):
    """Removes books that the user has already rented or purchased."""
    rented_books = set(RentalSchedule.objects.filter(user=user, returned=False).values_list("book", flat=True))
    purchased_books = set(PurchaseHistory.objects.filter(user=user).values_list("book", flat=True))
    
    return [book for book in books if book.id not in rented_books and book.id not in purchased_books]


def generate_book_recommendations(user):
    """
    Generates book recommendations based on the user's preferences and history.
    """

    top_rated_books = get_top_rated_books(user)
    popular_books = get_popular_books()
    similar_author_books = get_books_by_favorite_authors(
        user, exclude_books=[book.id for book in top_rated_books]
    )

    # Merge recommendations and filter unavailable books
    recommended_books = set(top_rated_books) | set(popular_books) | set(similar_author_books)
    filtered_books = filter_unavailable_books(user, recommended_books)

    # Remove old recommendations and create new ones
    BookRecommendation.objects.filter(user=user).delete()
    BookRecommendation.objects.bulk_create(
        [BookRecommendation(user=user, book=book) for book in filtered_books]
    )

    return filtered_books
