import pytest
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from accounts.models.verification import VerificationCode


@pytest.fixture
def valid_registration_data() -> dict:
    """
    Fixture to provide valid registration data.

    Returns:
        dict: A dictionary containing valid registration details.
    """
    return {
        "email": "testuser@example.com",
        "verification_code": "123456",
        "first_name": "Test",
        "last_name": "User",
        "password": "testpassword123"
    }


@pytest.fixture
def invalid_verification_code_data() -> dict:
    """
    Fixture to provide invalid verification code data.

    Returns:
        dict: A dictionary containing invalid verification code details.
    """
    return {
        "email": "testuser@example.com",
        "verification_code": "wrongcode",
        "first_name": "Test",
        "last_name": "User",
        "password": "testpassword123"
    }


@pytest.fixture
def create_verification_code(valid_registration_data) -> VerificationCode:
    """
    Fixture to create a verification code for the given valid registration data.

    Args:
        valid_registration_data (dict): A dictionary containing valid 
        registration data.

    Returns:
        VerificationCode: The created VerificationCode instance.
    """
    return VerificationCode.objects.create(
        email=valid_registration_data["email"],
        verification_code="123456"
    )


@pytest.mark.django_db
def test_register_view_success(
                        valid_registration_data: dict, 
                        create_verification_code: VerificationCode) -> None:
    """
    Test case for successful user registration.

    Args:
        valid_registration_data (dict): A dictionary containing valid 
        registration data.
        create_verification_code (VerificationCode): A fixture that provides a 
        valid verification code.

    Asserts:
        - Status code is 201 Created.
        - Registration success message is returned.
        - User is created and password is hashed correctly.
    """
    url = reverse("register")
    client = APIClient()
    response = client.post(
        url, 
        data=valid_registration_data, 
        format="json"
    )
    
    user = User.objects.filter(
        email=valid_registration_data["email"]
    ).first()
    
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["message"] == "Registration successful."
    assert user is not None
    assert user.check_password(valid_registration_data["password"])


@pytest.mark.django_db
def test_register_view_invalid_verification_code(
                                    invalid_verification_code_data: dict, 
                                    create_verification_code: VerificationCode) -> None:
    """
    Test case for invalid verification code during registration.

    Args:
        invalid_verification_code_data (dict): A dictionary containing invalid 
        verification code data.
        create_verification_code (VerificationCode): A fixture that provides a 
        valid verification code.

    Asserts:
        - Status code is 400 Bad Request.
        - Error message for the verification code is returned.
        - Error message for invalid verification code is shown.
    """
    url = reverse("register")
    client = APIClient()
    response = client.post(
        url, 
        data=invalid_verification_code_data, 
        format="json"
    )
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "verification_code" in response.data
    assert "Ensure this field has no more than 6 characters." in response.data["verification_code"]
