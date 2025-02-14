from accounts.models.verification import VerificationCode
from utils.verification_code import generate_verification_code

__all__ = ["create_verification_code"]


def create_verification_code(email):
    code = generate_verification_code()

    # Check and delete existing code
    VerificationCode.objects.filter(
        email=email, 
        is_verified=False
    ).delete()

    # Add the new code to the DB
    VerificationCode.objects.create(
        email=email,
        verification_code=code,
        is_verified=False
    )

    return code
