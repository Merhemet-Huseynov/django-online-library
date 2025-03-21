import pytest
from rest_framework.test import APIClient
from rest_framework import status

from books.models.catalog import Book, Category, Author 
from books.serializers.catalog import BookSerializer


@pytest.fixture
def api_client() -> APIClient:
    """
    Fixture to create an API client for testing.
    
    Returns:
        APIClient: The API client instance.
    """
    return APIClient()

@pytest.fixture
def author() -> Author:
    """
    Fixture to create an author instance.
    
    Returns:
        Author: The created Author instance.
    """
    return Author.objects.create(name="John Doe")

@pytest.fixture
def category() -> Category:
    """
    Fixture to create a category instance.
    
    Returns:
        Category: The created Category instance.
    """
    return Category.objects.create(name="Fiction")

@pytest.fixture
def book(author, category) -> Book:
    """
    Fixture to create a book instance with author and category.
    
    Returns:
        Book: The created Book instance.
    """
    return Book.objects.create(
        title="Test Book",
        slug="test-book",
        published_date="2025-01-01",
        condition="new",
        book_format="physical",
        author=author,     
        category=category     
    )

@pytest.mark.django_db
def test_book_list_view(api_client: APIClient, book: Book) -> None:
    """
    Test the book list API endpoint.
    
    Args:
        api_client (APIClient): The API client instance.
        book (Book): A sample book instance.
    
    Asserts:
        - Response status code is 200.
        - The response contains the expected book data.
    """
    response = api_client.get("/api/v1/books/")
    
    assert response.status_code == status.HTTP_200_OK
    expected_data = BookSerializer([book], many=True).data
    assert response.json() == expected_data

@pytest.mark.django_db
def test_book_detail_not_found(api_client: APIClient) -> None:
    """
    Test that requesting a non-existent book returns a 404 response.
    
    Args:
        api_client (APIClient): The API client instance.
    
    Asserts:
        - Response status code is 404.
    """
    response = api_client.get("/api/books/999/")
    
    assert response.status_code == status.HTTP_404_NOT_FOUND
