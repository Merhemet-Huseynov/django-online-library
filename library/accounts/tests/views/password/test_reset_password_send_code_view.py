import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from accounts.models.verification import VerificationCode
from unittest.mock import patch, MagicMock

pytestmark = pytest.mark.django_db


@pytest.fixture
def api_client() -> APIClient:
    """
    Fixture to initialize an APIClient instance for testing.

    Returns:
        APIClient: The instance of the APIClient.
    """
    return APIClient()


@pytest.fixture
def test_user() -> User:
    """
    Fixture to create a test user for authentication tests.

    Returns:
        User: The test user instance.
    """
    return User.objects.create_user(
        username="testuser", 
        email="test@example.com", 
        password="testpassword"
    )


@pytest.mark.django_db
def test_reset_password_send_code_success(api_client: APIClient, test_user: User) -> None:
    """
    Test for successfully sending a reset password verification code.

    Args:
        api_client (APIClient): The APIClient instance for making requests.
        test_user (User): The test user to trigger the password reset for.

    Asserts:
        - A 200 status code is returned.
        - The response contains the correct email and message.
        - A verification code is created in the database.
        - The email sending function is called once with the correct email.
    """
    with patch("services.auth.verification_service.send_verification_email.delay") as mock_send_email:
        response = api_client.post(
            "/api/accounts/reset-password-send-code/", 
            {
                "username": "testuser"
            }
        )

        assert response.status_code == 200
        assert response.data["email"] == "test@example.com"
        assert response.data["message"] == "Verification code sent."
        assert VerificationCode.objects.filter(email="test@example.com").exists()

        mock_send_email.assert_called_once_with("test@example.com")


@pytest.mark.django_db
def test_reset_password_send_code_invalid_user(api_client: APIClient) -> None:
    """
    Test for sending a reset password verification code to a non-existing user.

    Args:
        api_client (APIClient): The APIClient instance for making requests.

    Asserts:
        - A 400 status code is returned.
        - The error message indicates that the user does not exist.
    """
    response = api_client.post(
        "/api/accounts/reset-password-send-code/", 
        {
            "username": "nonexistent"
        }
    )

    assert response.status_code == 400
    assert "User with this username does not exist." in response.data["username"]


@pytest.mark.django_db
def test_reset_password_send_code_invalid_request(api_client: APIClient) -> None:
    """
    Test for sending a reset password verification code with an invalid request (missing username).

    Args:
        api_client (APIClient): The APIClient instance for making requests.

    Asserts:
        - A 400 status code is returned.
        - The response contains a missing "username" field.
    """
    response = api_client.post(
        "/api/accounts/reset-password-send-code/", 
        {}
    )

    assert response.status_code == 400
    assert "username" in response.data
