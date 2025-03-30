import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from payments.models import Payment
from payments.serializers import PaymentSerializer, PaymentCreateSerializer

# Initialize logger
logger = logging.getLogger(__name__)


class PaymentListCreateAPIView(APIView):
    """
    API view for retrieving a user's payments and creating a new payment.
    """
    permission_classes = [IsAuthenticated] 

    @swagger_auto_schema(
        operation_summary="List user payments",
        operation_description="Retrieve a list of payments belonging to the authenticated user.",
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="List of user payments",
                examples={
                    "application/json": [
                        {
                            "id": 1,
                            "amount": 100.00,
                            "status": "Completed",
                            "payment_date": "2024-03-30T12:00:00Z"
                        },
                        {
                            "id": 2,
                            "amount": 50.00,
                            "status": "Pending",
                            "payment_date": "2024-03-30T14:00:00Z"
                        }
                    ]
                }
            )
        },
        tags=["Payments"]
    )
    def get(self, request):
        """
        Retrieve only the authenticated user's payments.
        """
        payments = Payment.objects.filter(user=request.user)
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new payment",
        operation_description="Create a new payment record for the authenticated user.",
        request_body=PaymentCreateSerializer,
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                description="Payment created successfully",
                examples={
                    "application/json": {
                        "id": 3,
                        "amount": 200.00,
                        "status": "Pending",
                        "payment_date": "2024-03-30T15:00:00Z"
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
        serializer = PaymentCreateSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            try:
                payment = serializer.save(user=request.user)
                logger.info(f"Payment created successfully: {payment}")
                return Response(PaymentSerializer(payment).data, status=status.HTTP_201_CREATED)
            except Exception as e:
                logger.error(f"Payment creation failed: {str(e)}")
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        logger.error(f"Payment validation failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentDetailAPIView(APIView):
    """
    API view for retrieving, updating, or deleting a user's specific payment.
    """
    permission_classes = [IsAuthenticated]  

    def get_object(self, user, payment_id):
        """
        Helper function to retrieve a payment belonging to the authenticated user.
        """
        try:
            return Payment.objects.get(id=payment_id, user=user) 
        except Payment.DoesNotExist:
            return None

    @swagger_auto_schema(
        operation_summary="Retrieve user payment details",
        operation_description="Retrieve details of a specific payment belonging to the authenticated user.",
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Payment details",
                examples={
                    "application/json": {
                        "id": 1,
                        "amount": 100.00,
                        "status": "Completed",
                        "payment_date": "2024-03-30T12:00:00Z"
                    }
                }
            ),
            status.HTTP_404_NOT_FOUND: "Payment not found"
        },
        tags=["Payments"]
    )
    def get(self, request, payment_id):
        """
        Retrieve details of a specific payment belonging to the authenticated user.
        """
        payment = self.get_object(request.user, payment_id)
        if payment is None:
            return Response(
                {"detail": "Payment not found."}, 
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Delete a user payment",
        operation_description="Delete a specific payment if it belongs to the authenticated user and is pending.",
        responses={
            status.HTTP_204_NO_CONTENT: "Payment deleted successfully",
            status.HTTP_400_BAD_REQUEST: "Only pending payments can be deleted",
            status.HTTP_404_NOT_FOUND: "Payment not found"
        },
        tags=["Payments"]
    )
    def delete(self, request, payment_id):
        """
        Delete a specific payment if it belongs to the authenticated user and is still pending.
        """
        payment = self.get_object(request.user, payment_id)
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
        logger.info(f"User {request.user.id} deleted payment {payment_id}.")
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
