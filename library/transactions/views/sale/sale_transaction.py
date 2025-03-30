import logging
from rest_framework.views import APIView, Response, status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from transactions.serializers.sale import SaleTransactionSerializer
from transactions.models.sale import SaleTransaction

__all__ = [
    "SaleTransactionDetailView",
    "SaleTransactionListView"
]

# Logger initialization
logger = logging.getLogger(__name__)

User = get_user_model()


class SaleTransactionDetailView(APIView):
    """
    API view that allows only the user to view their own sale transactions.
    """

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Retrieve Sale Transaction Detail",
        operation_description=(
            "Fetches the sale transaction details for the authenticated user using the provided transaction ID (pk). "
            "If the transaction is not associated with the authenticated user, a 403 error is returned. "
            "If the transaction does not exist, a 404 error is returned."
        ),
        responses={
            200: openapi.Response(
                description="Sale transaction details retrieved successfully.",
                schema=SaleTransactionSerializer()
            ),
            403: openapi.Response(
                description="Unauthorized access attempt. The authenticated user does not have permission to view this transaction.",
                examples={
                    "application/json": {"detail": "You do not have permission to view this transaction."}
                }
            ),
            404: openapi.Response(
                description="Sale transaction not found.",
                examples={
                    "application/json": {"detail": "Not found."}
                }
            ),
        },
        tags=["Sale Transactions"]
    )
    def get(self, request, pk, *args, **kwargs):
        """
        Fetches the sale transaction by pk and returns 404 if not found.
        """
        sale_transaction = get_object_or_404(SaleTransaction, pk=pk)

        if sale_transaction.user != request.user:
            logger.warning(f"Unauthorized access attempt by user {request.user.username} to transaction {pk}")
            return Response(
                {"detail": "You do not have permission to view this transaction."},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = SaleTransactionSerializer(sale_transaction)
        logger.info(f"Sale transaction {pk} details retrieved successfully by user {request.user.username}")
        return Response(serializer.data, status=status.HTTP_200_OK)


class SaleTransactionListView(APIView):
    """
    API view that lists only the sale transactions of the authenticated user.
    """

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="List Sale Transactions",
        operation_description=(
            "Lists all sale transactions associated with the authenticated user. "
            "An optional query parameter 'user' can be provided to specify the username, "
            "but it must match the authenticated user, otherwise a 403 error is returned. "
            "If no transactions are found, a 404 error is returned."
        ),
        responses={
            200: openapi.Response(
                description="List of sale transactions retrieved successfully.",
                schema=SaleTransactionSerializer(many=True)
            ),
            403: openapi.Response(
                description="Unauthorized access attempt. The specified user does not match the authenticated user.",
                examples={
                    "application/json": {"detail": "You do not have permission to view this user's transactions."}
                }
            ),
            404: openapi.Response(
                description="No sale transactions found for the authenticated user.",
                examples={
                    "application/json": {"detail": "No sale transactions found."}
                }
            ),
        },
        tags=["Sale Transactions"]
    )
    def get(self, request, *args, **kwargs):
        """
        Only the authenticated user's sale transactions are shown.
        """
        user = request.query_params.get("user", None)

        if user:
            user_instance = get_object_or_404(User, username=user)

            if user_instance != request.user:
                logger.warning(f"Unauthorized access attempt by user {request.user.username} to {user_instance.username}'s transactions")
                return Response(
                    {"detail": "You do not have permission to view this user's transactions."},
                    status=status.HTTP_403_FORBIDDEN
                )

            sale_transactions = SaleTransaction.objects.filter(user=user_instance)
        else:
            sale_transactions = SaleTransaction.objects.filter(user=request.user)

        if not sale_transactions:
            logger.info(f"No sale transactions found for user {request.user.username}")
            return Response(
                {"detail": "No sale transactions found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = SaleTransactionSerializer(sale_transactions, many=True)
        logger.info(f"Sale transactions for user {request.user.username} retrieved successfully")
        return Response(serializer.data, status=status.HTTP_200_OK)
