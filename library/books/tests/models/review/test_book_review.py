import pytest
from django.contrib.auth.models import User
from books.models.catalog.book import Book
from books.models.review.book_review import BookReview
from books.models.catalog.author import Author
from books.models.catalog.category import Category


@pytest.mark.django_db
class TestBookReview:
    
    @pytest.fixture
    def user(self) -> User:
        """Create a user fixture for test purposes."""
        return User.objects.create_user(
            username="testuser", 
            password="password"
        )
    
    @pytest.fixture
    def book(self) -> Book:
        """Create a book fixture for test purposes."""
        author = Author.objects.create(name="Test Author")
        category = Category.objects.create(name="Test Category")
        return Book.objects.create(
            title="Test Book",
            author=author,
            category=category,
            published_date="2025-03-21",
        )

    def test_create_book_review(self) -> None:
        """Test creating a book review."""
        author = Author.objects.create(name="Test Author")
        category = Category.objects.create(name="Test Category")

        book = Book.objects.create(
            title="Test Book",
            author=author,
            category=category,
            published_date="2024-01-01"
        )

        user = User.objects.create_user(
            username="testuser", 
            password="password123"
        )

        review = BookReview.objects.create(
            book=book,
            user=user,
            rating=5,
            review="Great book!"
        )

        assert BookReview.objects.count() == 1
        assert review.book == book
        assert review.user == user
        assert review.rating == 5
        assert review.review == "Great book!"

    def test_review_rating_choices(self) -> None:
        """Test rating choices validation."""
        author = Author.objects.create(name="Test Author")
        category = Category.objects.create(name="Test Category")

        book = Book.objects.create(
            title="Test Book",
            author=author,
            category=category,
            published_date="2023-01-01"
        )

        user = User.objects.create_user(
            username="testuser", 
            password="testpassword"
        )

        review = BookReview.objects.create(
            book=book,
            user=user,
            rating=5,
            review="Great book!"
        )

        assert review.rating == 5
        assert review.review == "Great book!"
        assert str(review) == f"Review by testuser for Test Book - Rating: 5"
