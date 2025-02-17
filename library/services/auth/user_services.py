import random
import logging
from django.contrib.auth.models import User
from accounts.models.verification import VerificationCode

__all__ = [
    "validate_verification_code", 
    "generate_unique_username"
]

logger = logging.getLogger(__name__)


def validate_verification_code(email, verification_code):
    """
    Checks the accuracy and validity of the verification code.
    """
    logger.info(f"Validating verification code for email: {email}")
    try:
        record = VerificationCode.objects.get(
            email=email, 
            verification_code=verification_code
        )

    except VerificationCode.DoesNotExist:
        logger.warning(f"Invalid or expired verification code for email: {email}")
        raise ValueError(
            "Invalid or expired verification code."
        )

    if record.is_verified or record.is_expired():
        logger.warning(f"Verification code for email: {email} is either already verified or expired.")
        raise ValueError(
            "Verification code is invalid or expired."
        )

    logger.info(f"Verification code for email: {email} is valid.")
    return record

def generate_unique_username(base_username):
    """
    Generates a unique username. Suggests alternatives 
    if an existing username exists.
    """
    logger.info(f"Generating unique username based on: {base_username}")

    if not User.objects.filter(username=base_username).exists():
        logger.info(f"Username {base_username} is available.")
        return base_username

    suggested_usernames = []
    for _ in range(3):
        new_username = f"{base_username}{random.randint(100, 999)}"
        logger.info(f"Checking availability for username: {new_username}")

        if not User.objects.filter(username=new_username).exists():
            suggested_usernames.append(new_username)

    if suggested_usernames:
        logger.info(f"Suggested alternative usernames:", ", ".join(suggested_usernames))
        raise ValueError(
            f"Username \"{base_username}\" is already taken.",
            f"Try one of these:", ", ".join(suggested_usernames)
        )

    logger.warning(f"Could not find any available username alternatives for {base_username}.")
    raise ValueError(f"Username \"{base_username}\" is already taken and no alternatives are available.")
