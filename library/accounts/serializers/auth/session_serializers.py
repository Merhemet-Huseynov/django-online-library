from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        write_only=True
    )

    def validate(self, data):
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

        # We generate and return JWT tokens
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
