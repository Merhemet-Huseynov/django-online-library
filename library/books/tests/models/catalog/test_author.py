import pytest
from books.models.catalog import Author
from services.slug import generate_unique_slug


@pytest.mark.django_db
def test_slug_is_unique() -> None:
    """
    Test that the slug is created uniquely for authors with the same name.
    
    When two authors with the same name are created, their slugs should be different
    to ensure uniqueness.
    """
    author1 = Author.objects.create(
        name="Test Author"
    )
    author2 = Author.objects.create(
        name="Test Author"
    )
    
    assert author1.slug != author2.slug


@pytest.mark.django_db
def test_slug_remains_unchanged() -> None:
    """
    Test that the slug remains unchanged if it is set manually.
    
    If an author is created with a custom slug, calling save() should not alter 
    the slug value.
    """
    author = Author.objects.create(
        name="Test Author", 
        slug="custom-slug"
    )
    original_slug = author.slug
    author.save()
    assert author.slug == original_slug
