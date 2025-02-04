import random
from rest_framework import serializers
from django.contrib.auth.models import User
from books.models.auth.email_verification import VerificationCode

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    verification_code = serializers.CharField(min_length=6, max_length=6)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data["email"]
        verification_code = data["verification_code"]

        try:
            record = VerificationCode.objects.get(
                email=email, 
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
        validated_data.pop("verification_code")
        base_username = validated_data["first_name"]
        username = base_username
        counter = 1

        while User.objects.filter(username=username).exists():
            username = f"{base_username}{random.randint(100, 999)}"

        validated_data["username"] = username  
        user = User.objects.create_user(**validated_data)
        
        VerificationCode.objects.filter(
            email=validated_data["email"]
        ).update(is_verified=True)

        return user







    # def create(self, validated_data):
    #     validated_data["username"] = validated_data["email"]
    #     validated_data.pop("verification_code")
    #     user = User.objects.create_user(**validated_data)
    #     VerificationCode.objects.filter(
    #         email=validated_data["email"]
    #     ).update(is_verified=True)
    #     return user