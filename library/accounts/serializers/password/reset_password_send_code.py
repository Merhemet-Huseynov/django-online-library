from rest_framework import serializers
from django.contrib.auth.models import User

from services.auth import reset_password_send_code


class ResetPasswordSendCodeSerializer(serializers.Serializer):
    """
    Serializer for sending a password reset code to the user's email.
    Takes the username and validates if the user exists. If valid, sends the reset code.
    """
    username = serializers.CharField()

    def validate_username(self, value: str) -> str:
        """
        Validates the provided username. Checks if the user exists in the system.
        
        Args:
            value (str): The username to validate.

        Returns:
            str: The validated username if it exists.

        Raises:
            serializers.ValidationError: If the user does not exist.
        """
        try:
            user = User.objects.get(username=value)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                "User with this username does not exist."
            )

        self.user = user
        return value

    def create(self, validated_data: dict) -> None:
        """
        Creates a password reset request by sending a reset code to the user's email.

        Args:
            validated_data (dict): The validated data, which includes the user information.

        Returns:
            None: This method triggers the external function to send the reset code.
        """
        return reset_password_send_code(self.user.email)
