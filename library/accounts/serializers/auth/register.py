from rest_framework import serializers
from django.contrib.auth.models import User

from accounts.models.verification import VerificationCode
from services.auth import (
    validate_verification_code, 
    generate_unique_username
)


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    verification_code = serializers.CharField(
        min_length=6, 
        max_length=6
    )
    first_name = serializers.CharField(
        max_length=30
    )
    last_name = serializers.CharField(
        max_length=30
    )
    password = serializers.CharField(
        write_only=True
    )   

    def validate(self, data):
        try:
            validate_verification_code(
                data["email"], 
                data["verification_code"]
            )
        except ValueError as e:
            raise serializers.ValidationError(
                {"verification_code": str(e)}
            )

        return data

    def create(self, validated_data):
        validated_data.pop("verification_code")
        try:
            validated_data["username"] = generate_unique_username(
                validated_data["first_name"]
            )
        except ValueError as e:
            raise serializers.ValidationError(
                {"username": str(e)}
            )

        user = User.objects.create_user(**validated_data)
        
        VerificationCode.objects.filter(
            email=validated_data["email"]
        ).update(is_verified=True)

        return user
