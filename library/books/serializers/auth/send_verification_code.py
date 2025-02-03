from rest_framework import serializers
from books.models.auth.email_verification import VerificationCode
from books.utils.verification_code.verification_code import generate_verification_code

class SendVerificationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        VerificationCode.objects.filter(email=value).delete()
        return value

    def create(self, validated_data):
        email = validated_data["email"]
        verification_code = generate_verification_code(email)
        return {"email": email, "message": "Verification code sent."}
