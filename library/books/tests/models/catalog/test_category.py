import pytest
from django.db.utils import IntegrityError
from books.models.catalog import Category


@pytest.fixture
def super_category() -> Category:
    """Fixture for creating a super category"""
    return Category.objects.create(
        name="Super Category"
    )


@pytest.mark.django_db
def test_category_creation() -> None:
    """Test the creation of a category."""
    category: Category = Category.objects.create(
        name="Test Category"
    )
    assert category.name == "Test Category"
    assert category.is_active is True
    assert category.super_category is None
    assert category.order == 1


@pytest.mark.django_db
def test_subcategory_creation(super_category: Category) -> None:
    """Test the creation of a subcategory under a super category."""
    subcategory: Category = Category.objects.create(
        name="Subcategory 1", 
        super_category=super_category
    )
    assert subcategory.name == "Subcategory 1"
    assert subcategory.super_category == super_category
    assert subcategory.order == 1


@pytest.mark.django_db
def test_unique_slug_generation() -> None:
    """Test that slugs are unique for each category."""
    category1: Category = Category.objects.create(
        name="Unique Slug Category 1"
    )
    category2: Category = Category.objects.create(
        name="Unique Slug Category 2"
    )
    assert category1.slug != category2.slug


@pytest.mark.django_db
def test_order_increments_for_subcategories(super_category: Category) -> None:
    """Test that order increments correctly for subcategories."""
    subcategory1: Category = Category.objects.create(
        name="Subcategory 1", 
        super_category=super_category
    )
    subcategory2: Category = Category.objects.create(
        name="Subcategory 2", 
        super_category=super_category
    )
    assert subcategory1.order == 1
    assert subcategory2.order == 2


@pytest.mark.django_db
def test_subcategory_requires_active_super_category() -> None:
    """Test that a subcategory cannot be created under an inactive super category."""
    inactive_super_category: Category = Category.objects.create(
        name="Inactive Super Category", 
        is_active=False
    )
    with pytest.raises(ValueError):
        Category.objects.create(
            name="Subcategory under inactive category",
            super_category=inactive_super_category,
        )


@pytest.mark.django_db
def test_category_with_super_category(super_category: Category) -> None:
    """Test that a subcategory correctly links to its super category."""
    subcategory: Category = Category.objects.create(
        name="Subcategory 1", 
        super_category=super_category
    )
    assert subcategory.super_category == super_category


@pytest.mark.django_db
def test_unique_together_constraint(super_category: Category) -> None:
    """
    Test the unique together constraint for categories with the same 
    super category and order.
    """
    Category.objects.create(
        name="Category 1", 
        super_category=super_category, 
        order=1
    )

    with pytest.raises(IntegrityError):
        Category.objects.create(
            name="Category 2", 
            super_category=super_category, 
            order=1
        )


@pytest.mark.django_db
def test_category_icon_path() -> None:
    """Test that the icon field returns the correct file path."""
    category: Category = Category.objects.create(
        name="Fiction", 
        icon="fiction-icon"
    )
    assert str(category.icon) == "fiction-icon"
