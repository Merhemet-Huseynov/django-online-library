import pytest
from books.models.catalog import Author
from books.serializers.catalog import AuthorSerializer


@pytest.mark.django_db
def test_author_serializer_serialization():
    """AuthorSerializer should serialize the model object correctly."""
    author = Author.objects.create(
        name="Test Author",
        bio="Some biography",
        birth_date="1990-01-01",
        slug="test-author"
    )

    serializer = AuthorSerializer(author)
    expected_data = {
        "id": author.id,
        "name": "Test Author",
        "bio": "Some biography",
        "birth_date": "1990-01-01",
        "slug": "test-author"
    }

    assert serializer.data == expected_data


@pytest.mark.django_db
def test_author_serializer_deserialization():
    """AuthorSerializer should create an Author object from JSON data."""
    data = {
        "name": "New Author",
        "bio": "New author bio",
        "birth_date": "1985-05-15",
        "slug": "new-author"
    }

    serializer = AuthorSerializer(data=data)
    assert serializer.is_valid()
    author = serializer.save()

    assert author.name == "New Author"
    assert author.bio == "New author bio"
    assert str(author.birth_date) == "1985-05-15"
    assert author.slug == "new-author"


@pytest.mark.django_db
def test_author_serializer_validation():
    """AuthorSerializer should fail for an empty name."""
    data = {
        "name": "",
        "bio": "Test Bio",
        "birth_date": "1995-03-20",
        "slug": "invalid-author"
    }

    serializer = AuthorSerializer(data=data)
    assert not serializer.is_valid()
    assert "name" in serializer.errors
