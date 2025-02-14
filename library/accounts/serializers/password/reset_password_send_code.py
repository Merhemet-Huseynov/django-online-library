from rest_framework import serializers
from django.contrib.auth.models import User

from services.auth import reset_password_send_code


class ResetPasswordSendCodeSerializer(serializers.Serializer):
    username = serializers.CharField()

    def validate_username(self, value):
        try:
            user = User.objects.get(username=value)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                "User with this username does not exist."
            )

        self.user = user
        return value

    def create(self, validated_data):
        return reset_password_send_code(self.user.email)
