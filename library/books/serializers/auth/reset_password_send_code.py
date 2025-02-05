from rest_framework import serializers
from django.contrib.auth.models import User
from books.models.auth.email_verification import VerificationCode
from books.utils.verification_code import generate_verification_code
from books.tasks import send_verification_email

class ResetPasswordSendCodeSerializer(serializers.Serializer):
    username = serializers.CharField()

    def validate_username(self, value):
        try:
            user = User.objects.get(username=value)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                "User with this username does not exist."
            )

        self.user = user
        return value

    def create(self, validated_data):
        email = self.user.email  
        VerificationCode.objects.filter(email=email).delete()
        verification_code = generate_verification_code(email)

        VerificationCode.objects.create(
            email=email, 
            verification_code=verification_code
        )

        send_verification_email.delay(email)

        return {"email": email, "message": "Verification code sent."}