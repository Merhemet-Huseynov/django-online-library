import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from payments.models import Payment
from payments.serializers import PaymentSerializer

__all__ = [
    "PaymentListCreateAPIView",
    "PaymentDetailAPIView"
]

# Initialize logger
logger = logging.getLogger(__name__)


class PaymentListCreateAPIView(APIView):
    """
    API View to retrieve all payments and create a new payment.
    """
    @swagger_auto_schema(
        operation_summary="List all payments",
        operation_description="Retrieve a list of all payments.",
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="List of payments",
                examples={
                    "application/json": [
                        {
                            "id": 1,
                            "amount": 100.00,
                            "status": "Completed",
                            "created_at": "2024-03-30T12:00:00Z"
                        },
                        {
                            "id": 2,
                            "amount": 50.00,
                            "status": "Pending",
                            "created_at": "2024-03-30T14:00:00Z"
                        }
                    ]
                }
            )
        },
        tags=["Payments"]
    )
    def get(self, request):
        """
        List all payments in the system.
        """
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new payment",
        operation_description="Create a new payment record.",
        request_body=PaymentSerializer,
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                description="Payment created successfully",
                examples={
                    "application/json": {
                        "id": 3,
                        "amount": 200.00,
                        "status": "Pending",
                        "created_at": "2024-03-30T15:00:00Z"
                    }
                }
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request: Validation error"
        },
        tags=["Payments"]
    )
    def post(self, request):
        """
        Create a new payment.
        """
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            # Save payment and log the creation
            serializer.save()
            logger.info(f"Payment created successfully: {serializer.data}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(f"Payment creation failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentDetailAPIView(APIView):
    """
    API View to retrieve, update, or delete a payment.
    """

    def get_object(self, payment_id):
        """
        Helper function to get a payment object by its ID.
        """
        try:
            return Payment.objects.get(id=payment_id)
        except Payment.DoesNotExist:
            return None

    @swagger_auto_schema(
        operation_summary="Retrieve payment details",
        operation_description="Retrieve details of a specific payment.",
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Payment details",
                examples={
                    "application/json": {
                        "id": 1,
                        "amount": 100.00,
                        "status": "Completed",
                        "created_at": "2024-03-30T12:00:00Z"
                    }
                }
            ),
            status.HTTP_404_NOT_FOUND: "Payment not found"
        },
        tags=["Payments"]
    )
    def get(self, request, payment_id):
        """
        Retrieve a specific payment by its ID.
        """
        payment = self.get_object(payment_id)
        if payment is None:
            return Response(
                {"detail": "Payment not found."}, 
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Delete a payment",
        operation_description="Delete a specific payment if it is pending.",
        responses={
            status.HTTP_204_NO_CONTENT: "Payment deleted successfully",
            status.HTTP_400_BAD_REQUEST: "Only pending payments can be deleted",
            status.HTTP_404_NOT_FOUND: "Payment not found"
        },
        tags=["Payments"]
    )
    def delete(self, request, payment_id):
        """
        Delete a specific payment if it is pending.
        """
        payment = self.get_object(payment_id)
        if payment is None:
            return Response(
                {"detail": "Payment not found."}, 
                status=status.HTTP_404_NOT_FOUND
            )
        if payment.status != Payment.PENDING:
            return Response(
                {"detail": "Only pending payments can be deleted."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Log payment deletion
        logger.info(f"Payment with ID {payment_id} is being deleted.")
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
