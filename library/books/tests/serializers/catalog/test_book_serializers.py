import pytest
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from django.core.files.uploadedfile import SimpleUploadedFile
from typing import Dict, Any

from books.models.catalog import Book, Author, Category
from books.serializers.catalog import BookSerializer


@pytest.fixture
def author() -> Author:
    """
    Creates and returns an Author instance.
    
    :return: Author instance with predefined name and birth date.
    """
    return Author.objects.create(
        name="Author Name", 
        birth_date="1990-01-01"
    )


@pytest.fixture
def category() -> Category:
    """
    Creates and returns a Category instance.
    
    :return: Category instance with a predefined name.
    """
    return Category.objects.create(
        name="Category Name"
    )


@pytest.fixture
def book_data(author: Author, category: Category) -> Dict[str, Any]:
    """
    Provides sample book data for testing.
    
    :param author: Author instance for the book.
    :param category: Category instance for the book.
    :return: Dictionary containing book attributes.
    """
    return {
        "title": "Book Title",
        "isbn": "1234567890",
        "description": "Book Description",
        "published_date": "2025-01-01",
        "condition": "new",
        "book_format": "physical",
        "page_count": 200,
        "edition": "1st",
        "publisher": "Publisher Name",
        "language": "English",
        "shelf_location": "A1",
        "author": author.id,
        "category": category.id,
        "allow_rental": True,
        "available": True,
        "book_count": 5,
        "available_count": 5
    }


@pytest.fixture
def book_serializer(book_data: Dict[str, Any]) -> BookSerializer:
    """
    Creates and returns a BookSerializer instance initialized with sample book data.
    
    :param book_data: Sample book data.
    :return: BookSerializer instance.
    """
    return BookSerializer(data=book_data)


@pytest.mark.django_db
def test_book_serializer_valid(book_serializer: BookSerializer) -> None:
    """
    Tests the BookSerializer with valid data.

    - Ensures the serializer is valid.
    - Checks that the title and ISBN are correctly serialized.
    
    :param book_serializer: BookSerializer instance with valid data.
    """
    assert book_serializer.is_valid()
    assert book_serializer.validated_data["title"] == "Book Title"
    assert book_serializer.validated_data["isbn"] == "1234567890"


@pytest.mark.django_db
def test_book_serializer_invalid_isbn(book_serializer: BookSerializer) -> None:
    """
    Tests that an invalid ISBN raises a ValidationError.

    - Modifies ISBN to an invalid value.
    - Asserts that validation raises an exception.
    
    :param book_serializer: BookSerializer instance.
    """
    book_serializer.initial_data["isbn"] = "12345"  
    with pytest.raises(ValidationError):
        book_serializer.is_valid(raise_exception=True)

@pytest.mark.django_db
def test_book_serializer_required_fields() -> None:
    """
    Tests that missing required fields raise a ValidationError.

    - Passes an empty dictionary to the serializer.
    - Ensures that validation fails with appropriate errors.
    """
    book_data: Dict[str, Any] = {}  
    book_serializer = BookSerializer(data=book_data)
    
    with pytest.raises(serializers.ValidationError):
        book_serializer.is_valid(raise_exception=True)
