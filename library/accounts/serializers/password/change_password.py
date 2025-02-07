from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = self.context["request"].user 
        old_password = data.get("old_password")
        new_password = data.get("new_password")
        confirm_password = data.get("confirm_password")

        # Check if old password is correct
        if not authenticate(username=user.username, password=old_password):
            raise ValidationError(
                {"old_password": "The old password is incorrect."}
            )

        # Check if new password matches confirm password
        if new_password != confirm_password:
            raise ValidationError(
                {"new_password": "The new password and confirm password do not match."}
            )

        return data

    def create(self, validated_data):
        user = self.context["request"].user
        user.set_password(validated_data["new_password"])
        user.save()
        return user