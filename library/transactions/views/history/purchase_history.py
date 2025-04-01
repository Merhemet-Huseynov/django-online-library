import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from transactions.models.history import PurchaseHistory
from transactions.serializers.history import PurchaseHistorySerializer

__all__ = [
    "PurchaseHistoryListView",
    "PurchaseHistoryDetailView"
]

# Logging conf
logger = logging.getLogger(__name__)


class PurchaseHistoryListView(APIView):
    permission_classes = [IsAuthenticated] 

    @swagger_auto_schema(
        operation_description="Retrieve all purchase histories for the authenticated user",
        responses={200: PurchaseHistorySerializer(many=True)},
        tags=["PurchaseHistory"]
    )
    def get(self, request):
        """
        Retrieves all purchase histories of the authenticated user.

        This method checks for the logged-in user and retrieves all 
        purchase histories related to that user. If the user is not 
        authenticated, they will be denied access.

        Args:
            request (Request): The HTTP request object, which contains 
                               the authenticated user.

        Returns:
            Response: A response object containing the serialized 
                      purchase history data.

        Logs:
            Logs when a user successfully retrieves their purchase history.
        """
        purchase_histories = PurchaseHistory.objects.filter(user=request.user)
        serializer = PurchaseHistorySerializer(purchase_histories, many=True)
        logger.info(f"User {request.user.username} retrieved their purchase history.")
        
        return Response(serializer.data)


class PurchaseHistoryDetailView(APIView):
    permission_classes = [IsAuthenticated] 

    def get_object(self, pk, user):
        """
        Retrieves a purchase history record by ID for the specified user.

        This method attempts to retrieve a purchase history entry by 
        its ID and ensures it belongs to the authenticated user.

        Args:
            pk (int): The primary key of the purchase history entry.
            user (User): The authenticated user requesting the entry.

        Returns:
            PurchaseHistory: A purchase history record or None if not found.
        """
        try:
            return PurchaseHistory.objects.get(pk=pk, user=user)
        except PurchaseHistory.DoesNotExist:
            return None

    @swagger_auto_schema(
        operation_description="Retrieve a purchase history by ID for the authenticated user",
        responses={200: PurchaseHistorySerializer},
        tags=["PurchaseHistory"]
    )
    def get(self, request, pk):
        """
        Retrieves a single purchase history by ID for the authenticated user.

        This method checks if the authenticated user is requesting 
        their own purchase history entry by ID. If the entry does not 
        exist or belongs to another user, it returns a 404 error.

        Args:
            request (Request): The HTTP request object containing the 
                               authenticated user.
            pk (int): The primary key of the purchase history entry.

        Returns:
            Response: A response object with the serialized purchase 
                      history or an error message if not found.

        Logs:
            Logs when a user successfully retrieves a specific purchase history.
        """
        purchase_history = self.get_object(pk, request.user)
        if purchase_history is not None:
            serializer = PurchaseHistorySerializer(purchase_history)
            logger.info(f"User {request.user.username} retrieved purchase history ID {pk}.")
            return Response(serializer.data)
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_description="Delete a purchase history by ID for the authenticated user",
        responses={204: "No Content", 404: "Not Found"},
        tags=["PurchaseHistory"]
    )
    def delete(self, request, pk):
        """
        Deletes a single purchase history by ID for the authenticated user.

        This method checks if the authenticated user is trying to 
        delete their own purchase history entry by ID. If the entry 
        does not exist or belongs to another user, it returns a 404 error.

        Args:
            request (Request): The HTTP request object containing the 
                               authenticated user.
            pk (int): The primary key of the purchase history entry.

        Returns:
            Response: A response object confirming deletion or an error 
                      message if not found.

        Logs:
            Logs when a user deletes a specific purchase history.
        """
        purchase_history = self.get_object(pk, request.user)
        if purchase_history is not None:
            purchase_history.delete()
            logger.info(f"User {request.user.username} deleted purchase history ID {pk}.")
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
