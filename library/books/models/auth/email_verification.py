from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
import uuid

class VerificationCode(models.Model):
    email = models.EmailField() 
    verification_code = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return (now() - self.created_at).seconds > 180

    def __str__(self):
        return f"Verification code for {self.email}"

    class Meta:
        indexes = [
            models.Index(fields=["email"])
        ]
