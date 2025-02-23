import pytest
from django.utils.timezone import now
from datetime import timedelta

from accounts.models.verification import VerificationCode


@pytest.mark.django_db
def test_verification_code_creation() -> None:
    """
    Tests the creation of a VerificationCode object and checks if the 
    fields are correctly initialized.

    Asserts that the email, verification_code, is_verified, and created_at 
    fields are correctly set.
    """

    verification_code = VerificationCode.objects.create(
                            email="test@example.com",
                            verification_code="123456"
                        )

    assert verification_code.email == "test@example.com"
    assert verification_code.verification_code == "123456"
    assert verification_code.is_verified is False
    assert verification_code.created_at is not None


@pytest.mark.django_db
def test_is_expired() -> None:
    """
    Tests the is_expired method of the VerificationCode model.

    Asserts that is_expired returns False when the code is recent
    and True when the code has expired after 180 seconds.
    """

    verification_code = VerificationCode.objects.create(
                            email="test@example.com", 
                            verification_code="123456"
                        )             
    assert verification_code.is_expired() is False

    verification_code.created_at = now() - timedelta(seconds=181)
    verification_code.save()
    assert verification_code.is_expired() is True
