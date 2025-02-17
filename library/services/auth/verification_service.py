import logging
from accounts.models.verification import VerificationCode
from utils.verification_code import generate_verification_code
from accounts.tasks import send_verification_email

__all__ = ["reset_password_send_code"]

logger = logging.getLogger(__name__)

def reset_password_send_code(email):
    logger.info(f"Starting password reset process for email: {email}")
    
    verification_code = generate_verification_code()
    logger.debug(f"Generated verification code: {verification_code} for email: {email}")
    
    # Create verification code record in the database
    VerificationCode.objects.create(
        email=email, 
        verification_code=verification_code
    )
    logger.info(f"Verification code for {email} has been saved to the database.")
    
    # Send verification email asynchronously
    send_verification_email.delay(email)
    logger.info(f"Verification email sent to {email}.")

    return {"email": email, "message": "Verification code sent."}
