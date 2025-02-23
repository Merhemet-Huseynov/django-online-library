import pytest
from unittest.mock import patch, ANY
from django.contrib.auth.models import User

from services.auth.verification_service import reset_password_send_code
from accounts.serializers.password import ResetPasswordSendCodeSerializer
from accounts.models.verification import VerificationCode
from accounts.tasks import send_verification_email


@pytest.mark.django_db
def test_reset_password_send_code(email: str = "test@example.com") -> None:
    """
    Test the reset_password_send_code function to ensure it correctly:
    - Creates a verification code.
    - Calls the send_verification_email task.
    - Returns the correct response format.

    Args:
        email (str): The email to send the reset password verification code to.

    Asserts:
        - VerificationCode.objects.create is called once with the correct arguments.
        - send_verification_email.delay is called once with the correct email.
        - The function returns the expected response format.
    """
    with patch.object(VerificationCode.objects, "create") as mock_create, \
         patch.object(send_verification_email, "delay") as mock_send_email:

        response = reset_password_send_code(email)

        mock_create.assert_called_once_with(
            email=email, 
            verification_code=ANY
        )
        mock_send_email.assert_called_once_with(email)
        assert response == {"email": email, "message": "Verification code sent."}


@pytest.mark.django_db
def test_reset_password_send_code_serializer_valid() -> None:
    """
    Test the ResetPasswordSendCodeSerializer with valid data to ensure:
    - The serializer correctly validates when the username exists.
    
    Asserts:
        - The serializer is valid when the user exists.
    """
    user = User.objects.create(
                username="testuser", 
                email="test@example.com"
            )

    data = {"username": "testuser"}

    with patch("services.auth.verification_service.reset_password_send_code") as mock_reset:
        mock_reset.return_value = {
            "email": user.email, 
            "message": "Verification code sent."
        }

        serializer = ResetPasswordSendCodeSerializer(data=data)
        assert serializer.is_valid()


@pytest.mark.django_db
def test_reset_password_send_code_serializer_invalid() -> None:
    """
    Test the ResetPasswordSendCodeSerializer with invalid data to ensure:
    - The serializer correctly returns an error when the user does not exist.

    Asserts:
        - The serializer is invalid when the username does not exist.
        - The correct error message is returned for the "username" field.
    """
    data = {"username": "nonexistent"}

    serializer = ResetPasswordSendCodeSerializer(data=data)
    assert not serializer.is_valid()
    assert "username" in serializer.errors
    assert serializer.errors["username"][0] == "User with this username does not exist."
