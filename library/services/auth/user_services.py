import random
from django.contrib.auth.models import User
from accounts.models.verification import VerificationCode

__all__ = [
    "validate_verification_code", 
    "generate_unique_username"
]


def validate_verification_code(email, verification_code):
    """
    Checks the accuracy and validity of the verification code.
    """
    try:
        record = VerificationCode.objects.get(
            email=email, 
            verification_code=verification_code
        )

    except VerificationCode.DoesNotExist:
        raise ValueError(
            "Invalid or expired verification code."
        )

    if record.is_verified or record.is_expired():
        raise ValueError(
            "Verification code is invalid or expired."
        )

    return record

def generate_unique_username(base_username):
    """
    Generates a unique username. Suggests alternatives 
    if an existing username exists.
    """
    if not User.objects.filter(username=base_username).exists():
        return base_username

    suggested_usernames = []
    for _ in range(3):
        new_username = f"{base_username}{random.randint(100, 999)}"

        if not User.objects.filter(username=new_username).exists():
            suggested_usernames.append(new_username)

    raise ValueError(
        f"Username '{base_username}' is already taken. Try one of these: {', '.join(suggested_usernames)}"
    )
