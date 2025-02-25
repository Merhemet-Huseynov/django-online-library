import pytest
from rest_framework.test import APIClient
from rest_framework import status
from books.models.catalog import Author
from typing import List


@pytest.fixture
def api_client() -> APIClient:
    """Fixture for creating an API client.

    Returns:
        APIClient: The API client instance to use for making requests.
    """
    return APIClient()


@pytest.fixture
def authors() -> List[Author]:
    """Fixture for creating author instances.

    Returns:
        List[Author]: A list of created Author instances.
    """
    author1 = Author.objects.create(
        name="Author 1", 
        slug="author-1"
    )
    author2 = Author.objects.create(
        name="Author 2", 
        slug="author-2"
    )
    return [author1, author2]


@pytest.mark.django_db
def test_author_list_view(api_client: APIClient, authors: List[Author]) -> None:
    """Test the AuthorListViews endpoint.

    Args:
        api_client (APIClient): The API client to make requests.
        authors (List[Author]): List of authors to check against.

    Returns:
        None: Asserts that the response is correct.
    """
    url = "/api/v1/books/authors/list/"
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == len(authors)
    assert response.data[0]["name"] == authors[0].name


@pytest.mark.django_db
def test_author_detail_view_by_id(api_client: APIClient, authors: List[Author]) -> None:
    """Test the AuthorDetailViews endpoint for author by id.

    Args:
        api_client (APIClient): The API client to make requests.
        authors (List[Author]): List of authors to check against.

    Returns:
        None: Asserts that the response is correct.
    """
    url = f"/api/v1/books/authors/{authors[0].id}/"
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == authors[0].name


@pytest.mark.django_db
def test_author_detail_view_by_slug(api_client: APIClient, authors: List[Author]) -> None:
    """Test the AuthorDetailViews endpoint for author by slug.

    Args:
        api_client (APIClient): The API client to make requests.
        authors (List[Author]): List of authors to check against.

    Returns:
        None: Asserts that the response is correct.
    """
    url = f"/api/v1/books/authors/{authors[1].slug}/"
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == authors[1].name
