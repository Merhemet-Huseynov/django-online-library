import pytest
from books.models.catalog import Author
from books.serializers.catalog import AuthorSerializer
from rest_framework import serializers


@pytest.mark.django_db
def test_author_serializer_serialization() -> None:
    """
    Test the serialization of the Author model using the AuthorSerializer.

    Ensures that an Author object is correctly serialized to a dictionary 
    with the expected fields and values.
    """
    author = Author.objects.create(
        name="Test Author",
        bio="Some biography",
        birth_date="1990-01-01",
        slug="test-author"
    )

    serializer: AuthorSerializer = AuthorSerializer(author)
    
    expected_data: dict = {
        "id": author.id,
        "name": "Test Author",
        "bio": "Some biography",
        "birth_date": "1990-01-01",
        "slug": "test-author",
        "image": None
    }

    assert serializer.data == expected_data


@pytest.mark.django_db
def test_author_serializer_deserialization() -> None:
    """
    Test the deserialization of data into the Author model.

    Ensures that valid JSON data can be used to create an Author object 
    and that the created object contains the expected attributes.
    """
    data: dict = {
        "name": "New Author",
        "bio": "New author bio",
        "birth_date": "1985-05-15",
        "slug": "new-author",
        "image": None
    }

    serializer: AuthorSerializer = AuthorSerializer(data=data)
    assert serializer.is_valid()
    author: Author = serializer.save()

    assert author.name == "New Author"
    assert author.bio == "New author bio"
    assert str(author.birth_date) == "1985-05-15"
    assert author.slug == "new-author"


@pytest.mark.django_db
def test_author_serializer_validation() -> None:
    """
    Test the validation of the AuthorSerializer.

    Ensures that the serializer fails validation when required fields, 
    such as the name, are missing or empty.
    """
    data: dict = {
        "name": "",
        "bio": "Test Bio",
        "birth_date": "1995-03-20",
        "slug": "invalid-author",
        "image": None
    }

    serializer: AuthorSerializer = AuthorSerializer(data=data)
    assert not serializer.is_valid()
    assert "name" in serializer.errors
