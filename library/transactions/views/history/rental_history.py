import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from transactions.models.history import RentalHistory
from transactions.serializers.history import RentalHistorySerializer

__all__ = [
    "RentalHistoryListView",
    "RentalHistoryDetailView"
]

# Logging conf
logger = logging.getLogger(__name__)


class RentalHistoryListView(APIView):
    permission_classes = [IsAuthenticated] 

    @swagger_auto_schema(
        operation_description="Retrieve all rental histories for the authenticated user",
        responses={200: RentalHistorySerializer(many=True)},
        tags=["RentalHistory"]
    )
    def get(self, request):
        """
        Retrieves all rental histories of the authenticated user.

        Args:
            request (Request): The HTTP request object, which contains 
                               the authenticated user.

        Returns:
            Response: A response object containing the serialized 
                      rental history data.

        Logs:
            Logs when a user successfully retrieves their rental history.
        """
        rental_histories = RentalHistory.objects.filter(user=request.user)
        serializer = RentalHistorySerializer(rental_histories, many=True)
        logger.info(f"User {request.user.username} retrieved their rental history.")
        
        return Response(serializer.data)


class RentalHistoryDetailView(APIView):
    permission_classes = [IsAuthenticated] 

    def get_object(self, pk, user):
        """
        Retrieves a rental history record by ID for the specified user.

        Args:
            pk (int): The primary key of the rental history entry.
            user (User): The authenticated user requesting the entry.

        Returns:
            RentalHistory: A rental history record or None if not found.
        """
        try:
            return RentalHistory.objects.get(pk=pk, user=user)
        except RentalHistory.DoesNotExist:
            return None

    @swagger_auto_schema(
        operation_description="Retrieve a rental history by ID for the authenticated user",
        responses={200: RentalHistorySerializer},
        tags=["RentalHistory"]
    )
    def get(self, request, pk):
        """
        Retrieves a single rental history by ID for the authenticated user.

        Args:
            request (Request): The HTTP request object containing the 
                               authenticated user.
            pk (int): The primary key of the rental history entry.

        Returns:
            Response: A response object with the serialized rental 
                      history or an error message if not found.

        Logs:
            Logs when a user successfully retrieves a specific rental history.
        """
        rental_history = self.get_object(pk, request.user)
        if rental_history is not None:
            serializer = RentalHistorySerializer(rental_history)
            logger.info(f"User {request.user.username} retrieved rental history ID {pk}.")
            return Response(serializer.data)
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_description="Delete a rental history by ID for the authenticated user",
        responses={204: "No Content", 404: "Not Found"},
        tags=["RentalHistory"]
    )
    def delete(self, request, pk):
        """
        Deletes a single rental history by ID for the authenticated user.

        Args:
            request (Request): The HTTP request object containing the 
                               authenticated user.
            pk (int): The primary key of the rental history entry.

        Returns:
            Response: A response object confirming deletion or an error 
                      message if not found.

        Logs:
            Logs when a user deletes a specific rental history.
        """
        rental_history = self.get_object(pk, request.user)
        if rental_history is not None:
            rental_history.delete()
            logger.info(f"User {request.user.username} deleted rental history ID {pk}.")
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
