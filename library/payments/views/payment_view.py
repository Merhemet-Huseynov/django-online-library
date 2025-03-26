from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
import logging

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
        responses={status.HTTP_200_OK: PaymentSerializer(many=True)},
        operation_description="Retrieve a list of all payments."
    )
    def get(self, request):
        """
        List all payments in the system.
        """
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=PaymentSerializer,
        responses={status.HTTP_201_CREATED: PaymentSerializer},
        operation_description="Create a new payment record."
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
        responses={status.HTTP_200_OK: PaymentSerializer},
        operation_description="Retrieve details of a specific payment."
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
        responses={status.HTTP_204_NO_CONTENT: "No Content"},
        operation_description="Delete a specific payment if it is pending."
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
