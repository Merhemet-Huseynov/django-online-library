import pytest
from django.contrib.auth.models import User
from accounts.models.user import UserPreferences
from books.models.catalog import Category, Author
from accounts.serializers.user import UserPreferencesSerializer


@pytest.mark.django_db
def test_user_preferences_serializer() -> None:
    """
    Test the UserPreferencesSerializer to ensure it serializes 
    user preferences including favorite categories and authors correctly.
    """
    # Create test user
    user = User.objects.create(username="testuser")

    # Create category and author
    category = Category.objects.create(name="Fiction")
    author = Author.objects.create(name="John Doe")

    # Create user preferences and assign category and author
    preferences = UserPreferences.objects.create(user=user)
    preferences.favorite_categories.add(category)
    preferences.favorite_authors.add(author)

    # Serialize the preferences
    serializer = UserPreferencesSerializer(preferences)
    data = serializer.data

    # Assert the serialized data matches the created objects
    assert data["user"] == user.id
    assert "Fiction" in data["favorite_categories"]
    assert "John Doe" in data["favorite_authors"]
