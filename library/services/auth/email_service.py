import logging
from accounts.models.verification import VerificationCode
from utils.verification_code import generate_verification_code

__all__ = ["create_verification_code"]


logger = logging.getLogger(__name__)

def create_verification_code(email):
    code = generate_verification_code()
    logger.info(f"Generated verification code for email: {email}.")

    # Check and delete existing code
    deleted_count = VerificationCode.objects.filter(
        email=email, 
        is_verified=False
    ).delete()
    logger.info(
        f"Deleted {deleted_count[0]} existing verification code(s) for email: {email}."
    )

    # Add the new code to the DB
    VerificationCode.objects.create(
        email=email,
        verification_code=code,
        is_verified=False
    )
    logger.info(
        f"New verification code created and stored for email: {email}."
    )

    return code
