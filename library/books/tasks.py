from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from books.models.auth.email_verification import VerificationCode
import random
import string

@shared_task
def send_verification_email(user_id):
    user = User.objects.get(id=user_id)
    verification_code = "".join(random.choices(string.digits, k=6))
    
    # Add the verification code to the database
    verification_entry = VerificationCode.objects.create(
        user=user, 
        verification_code=verification_code
    )

    sender_email = config("EMAIL_HOST_USER")

    # Send email to Gmail
    send_mail(
        "Email Verification",
        f"Your verification code is: {verification_code}",
        sender_email, 
        [user.email],
        fail_silently=False,
    )
