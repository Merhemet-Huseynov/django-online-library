from django.db import models
from django.contrib.auth.models import User

class VerificationCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    verification_code  = models.CharField(max_length=6, unique=True)
    email = models.EmailField()
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Verification code for {self.email}"

