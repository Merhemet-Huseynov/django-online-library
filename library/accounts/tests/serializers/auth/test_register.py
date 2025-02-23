import pytest
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework import serializers

from accounts.models.verification import VerificationCode
from accounts.serializers.auth import RegisterSerializer
from services.auth import (
    validate_verification_code, 
    generate_unique_username
)


@pytest.mark.django_db
def test_valid_registration() -> None:
    """
    Test case for valid user registration using the RegisterSerializer.
    Ensures that:
    - The user is created successfully.
    - The verification code is marked as verified.
    - The username is generated correctly.
    - The password is hashed correctly.
    """
    email = "test@example.com"
    verification_code = "123456"
    first_name = "John"
    last_name = "Doe"
    password = "password123"

    VerificationCode.objects.create(
        email=email, 
        verification_code=verification_code, 
        is_verified=False
    )

    data = {
        "email": email,
        "verification_code": verification_code,
        "first_name": first_name,
        "last_name": last_name,
        "password": password,
    }

    serializer = RegisterSerializer(data=data)
    assert serializer.is_valid()

    user = serializer.save()

    assert User.objects.filter(email=email).exists()
    assert VerificationCode.objects.filter(email=email, is_verified=True).exists()
    assert user.username == f"{first_name}"
    assert user.check_password(password)


@pytest.mark.django_db
def test_invalid_verification_code() -> None:
    """
    Test case for invalid verification code during user registration.
    Ensures that if an invalid verification code is provided, 
    a validation error is raised.
    """
    email = "test@example.com"
    verification_code = "000000"
    first_name = "John"
    last_name = "Doe"
    password = "password123"

    VerificationCode.objects.create(
        email=email, 
        verification_code="123456", 
        is_verified=False
    )

    data = {
        "email": email,
        "verification_code": verification_code,
        "first_name": first_name,
        "last_name": last_name,
        "password": password,
    }

    serializer = RegisterSerializer(data=data)

    # Validate the serializer and check for the correct error message
    with pytest.raises(ValidationError) as excinfo:
        serializer.is_valid(raise_exception=True)

    assert "verification_code" in str(excinfo.value)
    assert "Invalid or expired verification code" in str(excinfo.value)