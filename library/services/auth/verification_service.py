from accounts.models.verification import VerificationCode
from utils.verification_code import generate_verification_code
from accounts.tasks import send_verification_email

__all__ = ["reset_password_send_code"]


def reset_password_send_code(email):
    verification_code = generate_verification_code()
    
    VerificationCode.objects.create(
        email=email, 
        verification_code=verification_code
    )
    
    send_verification_email.delay(email)
    
    return {"email": email, "message": "Verification code sent."}
