import pytest
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model

from books.models.review import BookReview
from books.models.catalog.book import Book
from books.serializers.review.book_review import BookReviewSerializer
from books.models.catalog.author import Author

User = get_user_model()

@pytest.mark.django_db
def test_book_review_serializer() -> None:
    """
    Test the serialization of a book review. The test ensures that 
    the `BookReviewSerializer` correctly serializes the data fields 
    of a book review instance, including the book title, user username, 
    rating, review, and created_at timestamp.

    This test creates a sample user, author, book, and book review,
    then checks if the serialized data matches the expected values.

    Returns:
        None
    """
    user = User.objects.create_user(
        username="testuser", 
        password="testpassword"
    )

    author = Author.objects.create(
        name="Test Author"
    )

    book = Book.objects.create(
        title="Test Book",
        author=author, 
        published_date="2025-01-01"
    )

    book_review = BookReview.objects.create(
        book=book,
        user=user,
        rating=5,
        review="Amazing book!"
    )

    serializer = BookReviewSerializer(book_review)

    assert serializer.data["book_title"] == "Test Book"
    assert serializer.data["user_username"] == "testuser"
    assert serializer.data["rating"] == 5
    assert serializer.data["review"] == "Amazing book!"
    assert "created_at" in serializer.data

@pytest.mark.django_db
def test_book_review_invalid_rating() -> None:
    """
    Test the validation of an invalid rating in the book review serializer.
    The test ensures that a rating greater than the valid maximum (5) triggers
    a validation error in the serializer.

    This test creates a sample user, author, book, and attempts to serialize 
    a book review with an invalid rating (6), expecting a `ValidationError`.

    Returns:
        None
    """
    user = User.objects.create_user(
        username="testuser", 
        password="testpassword"
    )

    author = Author.objects.create(
        name="Test Author"
    )

    book = Book.objects.create(
        title="Test Book",
        author=author, 
        published_date="2025-01-01"
    )
    
    data = {
        "book": book.id,
        "user": user.id,
        "rating": 6,  
        "review": "This should fail!"
    }

    serializer = BookReviewSerializer(data=data)

    with pytest.raises(ValidationError):  
        serializer.is_valid(raise_exception=True)
