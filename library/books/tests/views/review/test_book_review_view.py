import pytest
from rest_framework.test import APIClient
from rest_framework import status
from books.models.catalog.book import Book
from books.models.catalog.author import Author
from django.contrib.auth import get_user_model
from books.models.review import BookReview

User = get_user_model()


@pytest.fixture
def user() -> User:
    """Fixture to create and return a test user."""
    return User.objects.create_user(
        username="testuser", 
        password="password123"
    )

@pytest.fixture
def author() -> Author:
    """Fixture to create and return a test author."""
    return Author.objects.create(name="Test Author")

@pytest.fixture
def book(author: Author) -> Book:
    """Fixture to create and return a test book."""
    return Book.objects.create(
        title="Test Book",
        author=author, 
        isbn="1234567890123",
        published_date="2025-01-01"
    )

@pytest.fixture
def review(book: Book, user: User) -> BookReview:
    """Fixture to create and return a test review for a book."""
    return BookReview.objects.create(
        book=book,
        user=user,
        rating=5,
        review="This is a great book!"
    )

@pytest.fixture
def api_client() -> APIClient:
    """Fixture to create and return a new API client instance."""
    return APIClient()

@pytest.mark.django_db 
def test_get_reviews(api_client: APIClient, book: Book, review: BookReview) -> None:
    """
    Test retrieving reviews for a specific book.
    
    Args:
        api_client (APIClient): The API client instance.
        book (Book): The test book instance.
        review (BookReview): The test review instance for the book.
    """
    url = f"/api/v1/books/{book.id}/reviews/"
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1  

@pytest.mark.django_db
def test_post_review(api_client: APIClient, book: Book, user: User) -> None:
    """
    Test posting a review for a specific book.
    
    Args:
        api_client (APIClient): The API client instance.
        book (Book): The test book instance.
        user (User): The test user instance.
    """
    url = f"/api/v1/books/{book.id}/reviews/"
    data = {
        "rating": 4,
        "review": "Good book!"
    }
    api_client.force_authenticate(user=user)
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["rating"] == 4
    assert response.data["review"] == "Good book!"
    assert response.data["user_username"] == user.username
    assert response.data["book_title"] == book.title

@pytest.mark.django_db
def test_post_review_unauthenticated(api_client: APIClient, book: Book) -> None:
    """
    Test posting a review without authentication.
    
    Args:
        api_client (APIClient): The API client instance.
        book (Book): The test book instance.
    """
    url = f"/api/v1/books/{book.id}/reviews/"
    data = {
        "rating": 4,
        "review": "Good book!"
    }
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db 
def test_get_review_detail(api_client: APIClient, review: BookReview) -> None:
    """
    Test retrieving the details of a specific review.
    
    Args:
        api_client (APIClient): The API client instance.
        review (BookReview): The test review instance.
    """
    url = f"/api/v1/reviews/{review.id}/"
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["rating"] == review.rating
    assert response.data["review"] == review.review

@pytest.mark.django_db
def test_put_review(api_client: APIClient, review: BookReview, user: User) -> None:
    """
    Test updating a specific review.
    
    Args:
        api_client (APIClient): The API client instance.
        review (BookReview): The test review instance.
        user (User): The test user instance.
    """
    url = f"/api/v1/reviews/{review.id}/"
    data = {
        "rating": 4,
        "review": "Updated review text."
    }
    api_client.force_authenticate(user=user)
    response = api_client.put(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["rating"] == 4
    assert response.data["review"] == "Updated review text."

@pytest.mark.django_db
def test_put_review_unauthorized(api_client: APIClient, review: BookReview, user: User) -> None:
    """
    Test updating a review by an unauthorized user.
    
    Args:
        api_client (APIClient): The API client instance.
        review (BookReview): The test review instance.
        user (User): The test user instance.
    """
    url = f"/api/v1/reviews/{review.id}/"
    data = {
        "rating": 4,
        "review": "Updated review text."
    }
    api_client.force_authenticate(user=user)
    review.user = User.objects.create_user(username="otheruser", password="password123")
    review.save()
    response = api_client.put(url, data, format="json")
    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
def test_delete_review(api_client: APIClient, review: BookReview, user: User) -> None:
    """
    Test deleting a specific review.
    
    Args:
        api_client (APIClient): The API client instance.
        review (BookReview): The test review instance.
        user (User): The test user instance.
    """
    url = f"/api/v1/reviews/{review.id}/"
    api_client.force_authenticate(user=user)
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert BookReview.objects.count() == 0

@pytest.mark.django_db
def test_delete_review_unauthorized(api_client: APIClient, review: BookReview, user: User) -> None:
    """
    Test deleting a review by an unauthorized user.
    
    Args:
        api_client (APIClient): The API client instance.
        review (BookReview): The test review instance.
        user (User): The test user instance.
    """
    url = f"/api/v1/reviews/{review.id}/"
    api_client.force_authenticate(user=user)
    review.user = User.objects.create_user(username="otheruser", password="password123")
    review.save()
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN
