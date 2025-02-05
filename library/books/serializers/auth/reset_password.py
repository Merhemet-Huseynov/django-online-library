from rest_framework import serializers
from django.contrib.auth.models import User
from books.models.auth.email_verification import VerificationCode

class ResetPasswordSerializer(serializers.Serializer):
    username = serializers.CharField()
    verification_code = serializers.CharField(min_length=6, max_length=6)
    new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data["username"]
        verification_code = data["verification_code"]

        try:
            record = VerificationCode.objects.get(
                email=User.objects.get(username=username).email,
                verification_code=verification_code
            )
        except VerificationCode.DoesNotExist:
            raise serializers.ValidationError(
                {"verification_code": "Invalid or expired verification code."}
            )

        if record.is_verified or record.is_expired():
            raise serializers.ValidationError(
                {"verification_code": "Verification code is invalid or expired."}
            )

        return data

    def create(self, validated_data):
        username = validated_data["username"]
        new_password = validated_data["new_password"]
        
        # We find the user by username
        user = User.objects.get(username=username)
        user.set_password(new_password)
        user.save()

        # Mark the verification code as used
        VerificationCode.objects.filter(
            email=user.email
        ).update(is_verified=True)

        return user
