import pytest
from django.contrib.auth.models import User
from accounts.models.verification import VerificationCode
from rest_framework.exceptions import ValidationError
from rest_framework.test import APIClient
from rest_framework.response import Response


@pytest.fixture
def user() -> User:
    """
    Fixture to create a test user.

    Returns:
        User: A User instance for testing.
    """
    return User.objects.create_user(
        username="testuser", 
        email="test@example.com", 
        password="oldpassword"
    )

@pytest.fixture
def verification_code(user: User) -> VerificationCode:
    """
    Fixture to create a verification code for the user.

    Args:
        user (User): The user instance to associate with the verification code.

    Returns:
        VerificationCode: A VerificationCode instance for testing.
    """
    return VerificationCode.objects.create(
        email=user.email,
        verification_code="123456",
        is_verified=False
    )

@pytest.fixture
def client() -> APIClient:
    """
    Fixture to provide an instance of the Django test client.

    Returns:
        APIClient: The test client for making requests.
    """
    return APIClient()


@pytest.mark.django_db
def test_reset_password_success(
            client: APIClient, 
            user: User, 
            verification_code: VerificationCode) -> None:
    """
    Test case to verify that the password reset works successfully with a valid 
    verification code.

    Args:
        client (APIClient): The test client to simulate HTTP requests.
        user (User): The user whose password will be reset.
        verification_code (VerificationCode): The verification code instance used 
        for testing.
    """
    data = {
        "username": "testuser",
        "verification_code": "123456",
        "new_password": "newpassword123"
    }

    response: Response = client.post("/api/v1/accounts/reset-password/", data)

    assert response.status_code == 200

    user.refresh_from_db()
    assert user.check_password("newpassword123")

    verification_code.refresh_from_db()
    assert verification_code.is_verified


@pytest.mark.django_db
def test_reset_password_invalid_code(
                    client: APIClient, 
                    user: User, 
                    verification_code: VerificationCode) -> None:
    """
    Test case to verify the behavior when an invalid verification 
    code is provided.

    Args:
        client (APIClient): The test client to simulate HTTP requests.
        user (User): The user whose password is being reset.
        verification_code (VerificationCode): The verification code 
        instance used for testing.
    """
    data = {
        "username": "testuser",
        "verification_code": "654321", 
        "new_password": "newpassword123"
    }

    response: Response = client.post("/api/v1/accounts/reset-password/", data)

    assert response.status_code == 400
    assert response.data["verification_code"] == ["Invalid or expired verification code."]