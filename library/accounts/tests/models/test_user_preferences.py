import pytest
from datetime import date
from django.contrib.auth import get_user_model
from books.models.catalog import Book, Category, Author
from transactions.models.rental import RentalSchedule
from transactions.models.history import PurchaseHistory
from books.models.review import BookRecommendation
from accounts.models.user import UserPreferences


@pytest.mark.django_db
def test_user_preferences_creation() -> None:
    """
    Test that UserPreferences object is created correctly with 
    default empty preferences.
    """
    user = get_user_model().objects.create(username="testuser")
    preferences = UserPreferences.objects.create(user=user)

    assert preferences.user == user
    assert preferences.favorite_categories.count() == 0
    assert preferences.favorite_authors.count() == 0

@pytest.mark.django_db
def test_get_top_rated_books() -> None:
    """
    Test that get_top_rated_books returns books sorted by rating 
    in descending order.
    """
    user = get_user_model().objects.create(username="testuser")
    author = Author.objects.create(name="Test Author")

    book1 = Book.objects.create(
        title="Book 1",
        author=author,
        published_date=date.today()
    )
    book2 = Book.objects.create(
        title="Book 2",
        author=author,
        published_date=date.today()
    )

    # Add reviews with different ratings
    book1.reviews.create(user=user, rating=5)
    book2.reviews.create(user=user, rating=3)

    preferences = UserPreferences.objects.create(user=user)
    top_books = preferences.get_top_rated_books()

    assert len(top_books) == 2
    assert top_books[0] == book1  


@pytest.mark.django_db
def test_generate_book_recommendations() -> None:
    """
    Test that generate_book_recommendations returns a list.
    """
    user = get_user_model().objects.create(username="testuser")
    author = Author.objects.create(name="Test Author")

    Book.objects.create(
        title="Book 1",
        author=author,
        published_date=date.today()
    )
    Book.objects.create(
        title="Book 2",
        author=author,
        published_date=date.today()
    )

    preferences = UserPreferences.objects.create(user=user)
    recommendations = preferences.generate_book_recommendations()

    assert isinstance(recommendations, list)