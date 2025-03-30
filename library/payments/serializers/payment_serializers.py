from django.db import transaction
from rest_framework import serializers
from payments.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "id",
            "user",
            "book",
            "amount",
            "status",
            "payment_method",
            "provider",
            "payment_date",
            "transaction_id",
            "is_refunded",
            "metadata",
        ]
        read_only_fields = ["payment_date", "transaction_id", "is_refunded"]


class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["book", "amount", "payment_method"]

    def validate(self, attrs):
        """
        Validates if the payment can be processed.
        If payment fails, no record is saved to the database.

        Args:
            attrs (dict): The validated data.

        Raises:
            serializers.ValidationError: If payment fails.
        """
        if not self.process_payment(attrs["amount"]):
            raise serializers.ValidationError("Payment failed! Please try again.")
        return attrs

    def create(self, validated_data):
        """
        Creates a payment record in the database, processes the payment, and updates the payment status.

        Args:
            validated_data (dict): The validated data.

        Returns:
            Payment: The created payment instance.

        Raises:
            serializers.ValidationError: If any error occurs during the payment process or record creation.
        """
        try:
            with transaction.atomic():
                # Create the payment record in the database
                payment = Payment.objects.create(**validated_data)

                # Process the payment and get the result
                payment_successful, transaction_id = self.process_payment(payment.amount)
                if not payment_successful:
                    raise ValueError("Payment processing failed!")

                # Save the transaction ID and update the status to completed
                payment.transaction_id = transaction_id
                payment.status = Payment.COMPLETED
                payment.save(update_fields=["transaction_id", "status"])

                return payment
        except Exception as e:
            raise serializers.ValidationError({"error": str(e)})

    def process_payment(self, amount):
        """
        Simulates payment processing. In a real-world scenario, 
        this would interact with an actual payment gateway.

        Args:
            amount (float): The payment amount.

        Returns:
            tuple: A tuple containing a boolean indicating success or failure, and a transaction ID.
        """
        import random

        transaction_id = f"TXN{random.randint(100000, 999999)}"
        return random.choice([True, False]), transaction_id
