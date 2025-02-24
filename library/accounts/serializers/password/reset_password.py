from rest_framework import serializers
from django.contrib.auth.models import User

from accounts.models.verification import VerificationCode


class ResetPasswordSerializer(serializers.Serializer):
    """
    Serializer for handling the password reset process.
    Validates the username, verification code, and new password.
    """
    username = serializers.CharField()
    verification_code = serializers.CharField(
        min_length=6, 
        max_length=6
    )
    new_password = serializers.CharField(
        write_only=True
    )

    def validate(self, data: dict) -> dict:
        """
        Validate the provided data to ensure the verification code is correct
        and not expired.
        
        Args:
            data (dict): The input data containing username, verification_code, and new_password.
        
        Returns:
            dict: The validated data if everything is correct.
        
        Raises:
            serializers.ValidationError: If the verification code is invalid or expired.
        """
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

    def create(self, validated_data: dict) -> User:
        """
        Create a new password for the user after validation.
        
        Args:
            validated_data (dict): The validated data containing username and new password.
        
        Returns:
            User: The updated user object with the new password set.
        """
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
