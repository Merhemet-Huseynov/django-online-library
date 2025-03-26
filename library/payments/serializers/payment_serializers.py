from rest_framework import serializers
from django.db import transaction
from drf_yasg.utils import swagger_auto_schema

from payments.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """
    Serializer for handling Payment model operations.

    This serializer provides functionalities to:
    - Create a new payment instance with atomic transactions.
    - Update payment status and transaction_id safely.
    """

    class Meta:
        model = Payment
        fields = [
            "id", 
            "user", 
            "book", 
            "amount", 
            "status", 
            "payment_date", 
            "transaction_id"
        ]

    def create(self, validated_data):
        """
        Creates a new payment instance within an atomic transaction 
        to ensure data integrity.
        """
        with transaction.atomic():
            payment = Payment.objects.create(**validated_data)
            return payment

    def update(self, instance, validated_data):
        """Updates only the status and transaction_id fields of an existing payment."""
        with transaction.atomic():
            instance.status = validated_data.get("status", instance.status)
            instance.transaction_id = validated_data.get("transaction_id", instance.transaction_id)
            instance.save()
            return instance
