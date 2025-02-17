import pytest
from rest_framework.exceptions import ValidationError
from rest_framework.test import APIClient
from books.models.catalog import Category
from books.serializers.catalog import (
    CategorySerializer, 
    SubCategorySerializer
)


@pytest.fixture
def category_instance(db) -> Category:
    """
    Fixture to create a Category instance for testing.
    """
    return Category.objects.create(
        name="Fiction",
        slug="fiction",
        icon="fiction-icon",
        order=1,
        is_active=True,
        super_category=None
    )


@pytest.fixture
def sub_category_instance(db, category_instance: Category) -> Category:
    """
    Fixture to create a SubCategory instance for testing.
    """
    return Category.objects.create(
        name="Fantasy",
        slug="fantasy",
        icon="fantasy-icon",
        order=2,
        is_active=True,
        super_category=category_instance
    )


@pytest.mark.django_db
def test_category_serializer(category_instance: Category) -> None:
    """
    Test the serialization of the Category model using CategorySerializer.
    """
    serializer = CategorySerializer(category_instance)
    data = serializer.data
    
    assert data["id"] == category_instance.id
    assert data["name"] == category_instance.name
    assert data["slug"] == category_instance.slug
    assert data["icon"] == category_instance.icon.url
    assert data["order"] == category_instance.order
    assert data["is_active"] == category_instance.is_active
    assert data["super_category"] is None
    assert "super_category_name" in data


@pytest.mark.django_db
def test_sub_category_serializer(sub_category_instance: Category) -> None:
    """
    Test the serialization of the SubCategory model using SubCategorySerializer.
    """
    serializer = SubCategorySerializer(sub_category_instance)
    data = serializer.data
    
    assert data["id"] == sub_category_instance.id
    assert data["name"] == sub_category_instance.name
    assert data["slug"] == sub_category_instance.slug
    assert data["icon"] == sub_category_instance.icon.url 
    assert data["order"] == sub_category_instance.order
    assert data["is_active"] == sub_category_instance.is_active
    assert data["super_category"] == sub_category_instance.super_category.id


@pytest.mark.django_db
def test_sub_category_serializer_missing_super_category() -> None:
    """
    Test the SubCategorySerializer raises validation error when 
    the super_category field is missing.
    """
    invalid_data = {
        "name": "Fantasy",
        "slug": "fantasy",
        "icon": "fantasy-icon",
        "order": 2,
        "is_active": True,
        "super_category": None
    }
    
    serializer = SubCategorySerializer(data=invalid_data)
    
    with pytest.raises(ValidationError):
        serializer.is_valid(raise_exception=True)
