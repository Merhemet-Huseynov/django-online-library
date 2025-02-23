import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from typing import Tuple


@pytest.fixture
def create_user() -> User:
    """
    Fixture to create a test user.

    Returns:
        User: A User object representing the created test user.
    """
    user = User.objects.create_user(
        username="testuser",
        email="test@example.com",
        password="oldpassword123"
    )
    return user


@pytest.fixture
def authenticated_client(create_user: User) -> Tuple[APIClient, User]:
    """
    Fixture to create an authenticated API client.

    Args:
        create_user (User): The created test user.

    Returns:
        Tuple[APIClient, User]: A tuple containing the authenticated 
        client and the test user.
    """
    client = APIClient()
    client.force_authenticate(user=create_user)
    return client, create_user


@pytest.mark.django_db
def test_change_password_success(authenticated_client: Tuple[APIClient, User]) -> None:
    """
    Test case for successfully changing the password.

    Args:
        authenticated_client (Tuple[APIClient, User]): The authenticated client 
        and the test user.

    Asserts:
        - The response status is HTTP 200 OK.
        - The success message is returned.
        - The password is updated successfully.
    """
    client, user = authenticated_client
    response = client.post(
        "/api/accounts/change-password/",
        {
            "old_password": "oldpassword123",
            "new_password": "Newpassword123!",
            "confirm_password": "Newpassword123!"
        },
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data["message"] == "Password changed successfully."
    assert user.check_password("Newpassword123!")


@pytest.mark.django_db
def test_change_password_wrong_old_password(
                                    authenticated_client: Tuple[APIClient, User]) -> None:
    """
    Test case for attempting to change the password with a wrong old password.

    Args:
        authenticated_client (Tuple[APIClient, User]): The authenticated client and 
        the test user.

    Asserts:
        - The response status is HTTP 400 BAD REQUEST.
        - The "old_password" field is included in the response data.
    """
    client, _ = authenticated_client
    response = client.post(
        "/api/accounts/change-password/",
        {
            "old_password": "wrongpassword",
            "new_password": "Newpassword123!",
            "confirm_password": "Newpassword123!"
        },
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "old_password" in response.data


@pytest.mark.django_db
def test_change_password_mismatch_new_passwords(
                                    authenticated_client: Tuple[APIClient, User]) -> None:
    """
    Test case for attempting to change the password with mismatched new passwords.

    Args:
        authenticated_client (Tuple[APIClient, User]): The authenticated client and 
        the test user.

    Asserts:
        - The response status is HTTP 400 BAD REQUEST.
        - The "new_password" field is included in the response data.
    """
    client, _ = authenticated_client
    response = client.post(
        "/api/accounts/change-password/",
        {
            "old_password": "oldpassword123",
            "new_password": "Newpassword123!",
            "confirm_password": "DifferentPassword123!"
        },
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "new_password" in response.data
