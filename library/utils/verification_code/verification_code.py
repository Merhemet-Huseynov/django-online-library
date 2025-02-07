import random
from accounts.models.verification import VerificationCode

def generate_verification_code(email):
    code = str(random.randint(100000, 999999))
    VerificationCode.objects.create(
        email=email, 
        verification_code=code
    )
    return code
