import logging
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from transactions.models import RentalSchedule
from transactions.serializers import RentalScheduleSerializer

__all__ = [
    "RentalScheduleListCreateAPIView",
    "RentalScheduleDetailAPIView"
]

# Setting up logger
logger = logging.getLogger(__name__)


class RentalScheduleListCreateAPIView(APIView):
    def get_permissions(self):
        """
        Dynamically set permission classes based on the request method.
        GET method is open to all users, while POST requires authentication.
        """
        if self.request.method == "GET":
            return [AllowAny()]  
        return [IsAuthenticated()] 

    @swagger_auto_schema(
        operation_summary="Get rental schedules",
        operation_description="Retrieve a list of all rental schedules.",
        responses={
            200: RentalScheduleSerializer(many=True),
            401: "Unauthorized"
        },
        tags=["RentalSchedules"]
    )
    def get(self, request, *args, **kwargs):
        """
        Retrieve a list of rental schedules for the authenticated user.
        """
        logger.info(f"User {request.user.id} is requesting rental schedules.")
        rental_schedules = RentalSchedule.objects.filter(user=request.user) 
        serializer = RentalScheduleSerializer(rental_schedules, many=True)
        logger.info(f"Found {len(rental_schedules)} rental schedules for user {request.user.id}.")
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create rental schedule",
        operation_description="Create a new rental schedule. Requires authentication.",
        request_body=RentalScheduleSerializer,
        responses={
            201: RentalScheduleSerializer,
            400: "Bad request"
        },
        tags=["RentalSchedules"]
    )
    def post(self, request, *args, **kwargs):
        """
        Create a new rental schedule. Requires authentication for access.
        The schedule can only be created by the authenticated user for themselves.
        """
        logger.info(f"User {request.user.id} is attempting to create a new rental schedule.")
        
        # Add the user to the request data before saving
        data = request.data.copy()  
        data['user'] = request.user.id 
        
        serializer = RentalScheduleSerializer(data=data)
        if serializer.is_valid():
            rental_schedule = serializer.save(user=request.user)  
            try:
                rental_schedule.rent_book() 
                logger.info(f"Rental schedule created successfully for user {request.user.id}.")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                logger.error(f"Error while processing rental for user {request.user.id}: {str(e)}")
                return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        logger.error(f"Invalid data provided for user {request.user.id}: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RentalScheduleDetailAPIView(APIView):
    def get_permissions(self):
        """
        Dynamically set permission classes based on the request method.
        GET method is open to all users, while other methods require authentication.
        """
        if self.request.method == "GET":
            return [AllowAny()] 
        return [IsAuthenticated()] 

    @swagger_auto_schema(
        operation_summary="Get rental schedule",
        operation_description="Retrieve a specific rental schedule by its primary key (pk). Available to all users for GET requests.",
        responses={
            200: RentalScheduleSerializer,
            404: "Not found"
        },
        tags=["RentalSchedules"]
    )
    def get(self, request, pk, *args, **kwargs):
        """
        Retrieve a specific rental schedule for the authenticated user.
        """
        logger.info(f"User {request.user.id} is requesting rental schedule with ID {pk}.")
        rental_schedule = get_object_or_404(RentalSchedule, pk=pk, user=request.user) 
        serializer = RentalScheduleSerializer(rental_schedule)
        logger.info(f"Rental schedule {pk} retrieved for user {request.user.id}.")
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Delete rental schedule",
        operation_description="Delete a specific rental schedule by its primary key (pk). Requires authentication.",
        responses={
            204: "No Content",
            404: "Not found"
        },
        tags=["RentalSchedules"]
    )
    def delete(self, request, pk, *args, **kwargs):
        """
        Delete a specific rental schedule. Requires authentication.
        Only the user who created the rental schedule can delete it.
        """
        logger.info(f"User {request.user.id} is attempting to delete rental schedule with ID {pk}.")
        rental_schedule = get_object_or_404(RentalSchedule, pk=pk, user=request.user) 
        rental_schedule.delete()
        logger.info(f"Rental schedule {pk} deleted successfully by user {request.user.id}.")
        return Response({"detail": "RentalSchedule deleted."}, status=status.HTTP_204_NO_CONTENT)
