import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.response import Response

User = get_user_model()


@pytest.fixture
def create_user() -> User:
    """
    Fixture to create a test user.

    Returns:
        User: The created user instance.
    """
    return User.objects.create_user(
        username="testuser",
        email="testuser@example.com",
        password="password123"
    )


@pytest.fixture
def client() -> APIClient:
    """
    Fixture to create an APIClient instance.

    Returns:
        APIClient: The client to interact with the API endpoints.
    """
    return APIClient()


@pytest.mark.django_db
def test_login_success(client: APIClient, create_user: User) -> None:
    """
    Test the login functionality with valid credentials.

    Args:
        client (APIClient): The client to send requests.
        create_user (User): The user to authenticate.

    Asserts:
        - The response status is HTTP 200 OK.
        - The response contains an access token.
    """
    login_data = {
        "username": "testuser",
        "password": "password123"
    }

    response: Response = client.post(
        "/api/accounts/login/", 
        login_data, 
        format="json"
    )

    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data


@pytest.mark.django_db
def test_login_invalid_credentials(client: APIClient, create_user: User) -> None:
    """
    Test the login functionality with invalid credentials.

    Args:
        client (APIClient): The client to send requests.
        create_user (User): The user to authenticate.

    Asserts:
        - The response status is HTTP 400 BAD REQUEST.
        - The response contains error message details.
    """
    login_data = {
        "username": "testuser",
        "password": "wrongpassword"
    }

    response: Response = client.post(
        "/api/accounts/login/", 
        login_data, 
        format="json"
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "non_field_errors" in response.data or "detail" in response.data  


@pytest.mark.django_db
def test_login_missing_credentials(client: APIClient) -> None:
    """
    Test the login functionality when credentials are missing.

    Args:
        client (APIClient): The client to send requests.

    Asserts:
        - The response status is HTTP 400 BAD REQUEST.
        - The response contains error messages for missing 
          username/email and password.
    """
    login_data = {}

    response: Response = client.post(
        "/api/accounts/login/", 
        login_data, 
        format="json"
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "username" in response.data or "email" in response.data
    assert "password" in response.data  
