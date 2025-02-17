import pytest
from rest_framework.test import APIClient
from django.test import Client
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from typing import Tuple

from books.models.catalog import Category


@pytest.fixture
def client() -> APIClient:
    """Fixture to provide a test client.

    Returns:
        APIClient: The test client for making API requests.
    """
    return APIClient()


@pytest.fixture
def category() -> Category:
    """Fixture to create a category.

    Returns:
        Category: The created category instance.
    """
    return Category.objects.create(
        name="Fiction",
        slug="fiction"
    )


@pytest.mark.django_db
def test_category_list_view(client: APIClient) -> None:
    """Test for CategoryListViews.

    Args:
        client (APIClient): The test client for making API requests.

    Asserts:
        The response status code is 200 OK and the response data is a list.
    """
    response: Response = client.get("/api/books/categories/list")

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)


@pytest.mark.django_db
def test_category_detail_view_by_id(client: APIClient, category: Category) -> None:
    """Test for CategoryDetailViews when retrieving category by ID.

    Args:
        client (APIClient): The test client for making API requests.
        category (Category): The category instance to test.

    Asserts:
        The response status code is 200 OK, and the returned category matches the requested ID.
    """
    response: Response = client.get(f"/api/books/categories/detail/{category.id}/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == category.id
    assert response.data["name"] == category.name


@pytest.mark.django_db
def test_category_detail_view_by_slug(client: APIClient, category: Category) -> None:
    """Test for CategoryDetailViews when retrieving category by slug.

    Args:
        client (APIClient): The test client for making API requests.
        category (Category): The category instance to test.

    Asserts:
        The response status code is 200 OK, and the returned 
        category matches the requested slug.
    """
    response: Response = client.get(f"/api/books/categories/detail/{category.slug}/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["slug"] == category.slug
    assert response.data["name"] == category.name


@pytest.mark.django_db
def test_category_detail_view_not_found(client: APIClient) -> None:
    """Test for CategoryDetailViews with invalid identifier.

    Args:
        client (APIClient): The test client for making API requests.

    Asserts:
        The response status code is 404 Not Found when the category does not exist.
    """
    response: Response = client.get("/api/books/categories/detail/invalid-id/")

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.fixture
def setup_categories() -> Tuple[Category, Category]:
    """Fixture to create categories and subcategories."""
    category1 = Category.objects.create(name="Category 1", slug="category-1")
    category2 = Category.objects.create(name="Category 2", slug="category-2")
    
    Category.objects.create(name="Subcategory 1", super_category=category1)
    Category.objects.create(name="Subcategory 2", super_category=category1)
    Category.objects.create(name="Subcategory 3", super_category=category2)

    return category1, category2


@pytest.mark.django_db
def test_get_subcategories_by_id_success(
        setup_categories: Tuple[Category, Category], client: Client
    ) -> None:

    """Test retrieving subcategories for a given category using ID."""
    category1, _ = setup_categories
    url: str = reverse("subcategories-list", kwargs={"super_category_name": category1.id})
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)
    assert len(response.data) == 2
    assert response.data[0]["name"] == "Subcategory 1"
    assert response.data[1]["name"] == "Subcategory 2"


@pytest.mark.django_db
def test_get_subcategories_by_slug_success(
        setup_categories: Tuple[Category, Category], client: Client
    ) -> None:
    
    """Test retrieving subcategories for a given category using slug."""
    category1, _ = setup_categories
    url: str = reverse("subcategories-list", kwargs={"super_category_name": category1.slug})
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)
    assert len(response.data) == 2
    assert response.data[0]["name"] == "Subcategory 1"
    assert response.data[1]["name"] == "Subcategory 2"


@pytest.mark.django_db
def test_get_subcategories_category_not_found(client: Client) -> None:
    """Test when the category ID or slug does not exist."""
    url: str = reverse("subcategories-list", kwargs={"super_category_name": "non-existent"})
    response = client.get(url)

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_get_subcategories_empty(setup_categories: Tuple[Category, Category], client: Client) -> None:
    """Test when a category has no subcategories."""
    _, category2 = setup_categories
    url: str = reverse("subcategories-list", kwargs={"super_category_name": category2.id})
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)
    assert len(response.data) == 1
    assert response.data[0]["name"] == "Subcategory 3"
