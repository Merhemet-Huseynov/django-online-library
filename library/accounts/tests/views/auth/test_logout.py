import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()  


@pytest.fixture
def create_user() -> User:
    """
    Creates and returns a test user.

    Returns:
        User: A test user instance.
    """
    return User.objects.create_user(
        email="test@example.com", 
        password="password123", 
        username="testuser"
    )
    
    
@pytest.fixture
def auth_client(create_user: User) -> tuple[APIClient, str]:
    """
    Creates an authenticated client with a valid refresh token.

    Args:
        create_user (User): The test user instance.

    Returns:
        tuple[APIClient, str]: A tuple containing the API client and the refresh token.
    """
    client = APIClient()
    refresh = RefreshToken.for_user(create_user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {str(refresh.access_token)}")
    return client, str(refresh)


@pytest.mark.django_db
def test_logout_success(auth_client: tuple[APIClient, str]) -> None:
    """
    Tests successful logout when a valid refresh token is provided.

    Args:
        auth_client (tuple[APIClient, str]): The authenticated client and refresh token.
    """
    client, refresh_token = auth_client
    url = reverse("logout")

    response: Response = client.post(
        url, 
        {
            "refresh": refresh_token
        }, 
        format="json"
    )

    assert response.status_code == 200
    assert response.data["detail"] == "Successfully logged out."


@pytest.mark.django_db
def test_logout_without_token() -> None:
    """
    Tests logout attempt without providing a refresh token.

    The API should return a 400 Bad Request response.
    """
    client = APIClient()
    url = reverse("logout")

    response: Response = client.post(
        url, 
        {}, 
        format="json"
    )

    assert response.status_code == 400
    assert response.data["detail"] == "Refresh token is required."


@pytest.mark.django_db
def test_logout_invalid_token() -> None:
    """
    Tests logout attempt with an invalid refresh token.

    The API should return a 400 Bad Request response.
    """
    client = APIClient()
    url = reverse("logout")

    response: Response = client.post(
        url, 
        {
            "refresh": "invalidtoken"
        }, 
        format="json"
    )

    assert response.status_code == 400
    assert response.data["detail"] == "Invalid token."
