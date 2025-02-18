from django.db import models
from django.utils.timezone import now


class VerificationCode(models.Model):
    email = models.EmailField()
    verification_code = models.CharField(
        max_length=6
    )
    is_verified = models.BooleanField(
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        indexes = [
            models.Index(fields=["email"]),
            models.Index(fields=["verification_code"]),
        ]

    def __str__(self):
        return f"Verification code for {self.email}"
    
    def is_expired(self):
        return (now() - self.created_at).total_seconds() > 180
