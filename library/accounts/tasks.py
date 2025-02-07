from celery import shared_task
from django.core.mail import send_mail
from accounts.models.verification import VerificationCode
from utils.verification_code import generate_verification_code
from decouple import config

@shared_task
def send_verification_email(email):
    verification_code = generate_verification_code(email)
    sender_email = config("EMAIL_HOST_USER")

    send_mail(
        "Email Verification",
        f"Your verification code is: {verification_code}",
        sender_email,
        [email],
        fail_silently=False,
    )
