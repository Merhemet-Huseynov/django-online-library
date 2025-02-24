from rest_framework import serializers

from accounts.models.verification import VerificationCode
from services.auth import create_verification_code


class SendVerificationCodeSerializer(serializers.Serializer):
    """
    Serializer for sending a verification code to the provided email address.
    
    Validates the email and creates a verification code.
    """
    email = serializers.EmailField()

    def validate_email(self, value: str) -> str:
        """
        Validates the email address. If an existing verification code exists for 
        the email, it is deleted before proceeding with new code creation.
        
        Args:
            value (str): The email address to be validated.

        Returns:
            str: The validated email address.
        """
        VerificationCode.objects.filter(email=value).delete()
        return value

    def create(self, validated_data: dict) -> dict:
        """
        Creates and sends a verification code to the given email address.
        
        Args:
            validated_data (dict): The validated data containing the email.

        Returns:
            dict: A dictionary containing the email and a success message.
        """
        email = validated_data["email"]
        verification_code = create_verification_code(email)
        return {"email": email, "message": "Verification code sent."}
