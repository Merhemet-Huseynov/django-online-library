import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.response import Response


@pytest.mark.django_db
def test_change_password_success() -> None:
    """
    Test that the user can successfully change their password.
    
    1. Creates a user with a specific old password.
    2. Authenticates the user.
    3. Sends a request to change the password with the correct old password.
    4. Verifies the password has been changed and the response status is 200.
    """
    user = User.objects.create_user(
                username="testuser", 
                password="oldpassword"
            )
    client = APIClient()
    client.force_authenticate(user=user)

    response: Response = client.post(
        "/api/accounts/change-password/", 
        {
            "old_password": "oldpassword",
            "new_password": "newsecurepassword",
            "confirm_password": "newsecurepassword",
        },
        format="json",
    )
    
    user.refresh_from_db()
    assert response.status_code == 200
    assert user.check_password("newsecurepassword")


@pytest.mark.django_db
def test_change_password_wrong_old_password() -> None:
    """
    Test that the user cannot change the password if the old password is incorrect.
    
    1. Creates a user with a specific old password.
    2. Authenticates the user.
    3. Sends a request to change the password with an incorrect old password.
    4. Verifies the response contains an error for the old password field.
    """
    user = User.objects.create_user(
                username="testuser", 
                password="oldpassword"
            )
    client = APIClient()
    client.force_authenticate(user=user)

    response: Response = client.post(
        "/api/accounts/change-password/",
        {
            "old_password": "wrongpassword",
            "new_password": "newsecurepassword",
            "confirm_password": "newsecurepassword",
        },
        format="json",
    )

    assert response.status_code == 400
    assert "old_password" in response.data


@pytest.mark.django_db
def test_change_password_mismatch() -> None:
    """
    Test that the user cannot change the password if the new passwords do not match.
    
    1. Creates a user with a specific old password.
    2. Authenticates the user.
    3. Sends a request to change the password with mismatched new passwords.
    4. Verifies the response contains an error for the new password field.
    """
    user = User.objects.create_user(
                username="testuser",  
                password="oldpassword"
            )
    client = APIClient()
    client.force_authenticate(user=user)

    response: Response = client.post(
        "/api/accounts/change-password/",
        {
            "old_password": "oldpassword",
            "new_password": "newsecurepassword",
            "confirm_password": "differentpassword",
        },
        format="json",
    )

    assert response.status_code == 400
    assert "new_password" in response.data
