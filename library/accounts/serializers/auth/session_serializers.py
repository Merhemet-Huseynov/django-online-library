from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login to authenticate and generate JWT tokens.
    """
    username = serializers.CharField()
    password = serializers.CharField(
        write_only=True
    )

    def validate(self, data: dict) -> dict:
        """
        Validates the provided username and password and generates JWT tokens.

        Args:
            data (dict): The validated data containing "username" and "password".

        Returns:
            dict: A dictionary containing "refresh" and "access" tokens.

        Raises:
            serializers.ValidationError: If the username or password is invalid.
        """
        username = data.get("username")
        password = data.get("password")

        # Authenticate the user with username and password
        user = authenticate(
            username=username, 
            password=password
        )

        if not user:
            raise serializers.ValidationError(
                "Invalid username or password."
            )

        # Generate and return JWT tokens
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


class LogoutSerializer(serializers.Serializer):
    """
    Serializer for user logout to handle the refresh token.
    """
    refresh = serializers.CharField()