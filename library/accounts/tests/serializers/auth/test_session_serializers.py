import pytest
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from accounts.serializers.auth import LoginSerializer


@pytest.fixture
def user() -> User:
    """
    Fixture to create and return a test user.

    Returns:
        User: A Django User object for testing.
    """
    return User.objects.create_user(
        username="testuser", 
        password="testpassword"
    )


@pytest.mark.django_db
def test_login_serializer_valid_credentials(user: User) -> None:
    """
    Test that the LoginSerializer returns valid JWT tokens for valid credentials.

    Args:
        user (User): A test user object created by the fixture.

    Asserts:
        - The serializer is valid.
        - The response contains refresh and access tokens.
    """
    data = {
        "username": "testuser",
        "password": "testpassword"
    }
    serializer = LoginSerializer(data=data)
    
    assert serializer.is_valid(), f"Serializer errors: {serializer.errors}"
    
    # Check if refresh and access tokens are returned
    tokens = serializer.validated_data
    assert "refresh" in tokens
    assert "access" in tokens


@pytest.mark.django_db
def test_login_serializer_invalid_credentials(user: User) -> None:
    """
    Test that the LoginSerializer raises a ValidationError for invalid credentials.

    Args:
        user (User): A test user object created by the fixture.

    Asserts:
        - A ValidationError is raised for invalid credentials.
    """
    data = {
        "username": "testuser",
        "password": "wrongpassword"
    }
    serializer = LoginSerializer(data=data)
    
    with pytest.raises(ValidationError):
        serializer.is_valid(raise_exception=True)
