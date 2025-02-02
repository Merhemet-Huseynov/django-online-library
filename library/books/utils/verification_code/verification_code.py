import random
from books.models.auth.email_verification import VerificationCode

def create_verification_code(email):
    code = str(random.randint(100000, 999999))  
    verification_code = VerificationCode.objects.create(code=code, email=email)
    return verification_code
