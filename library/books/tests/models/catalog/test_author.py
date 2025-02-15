import pytest
from books.models.catalog import Author
from services.slug import generate_unique_slug


@pytest.mark.django_db
def test_slug_is_unique():
    """The slug should be created differently for authors with the same name."""
    author1 = Author.objects.create(
        name="Test Author"
    )
    author2 = Author.objects.create(
        name="Test Author"
    )
    
    assert author1.slug != author2.slug


@pytest.mark.django_db
def test_slug_remains_unchanged():
    """If the slug is set, it should not change when save() is called."""
    author = Author.objects.create(
        name="Test Author", 
        slug="custom-slug"
    )
    original_slug = author.slug
    author.save()
    assert author.slug == original_slug
