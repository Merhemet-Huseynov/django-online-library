import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from event_manager.models.event import EventSchedule
from event_manager.serializers.event import EventScheduleSerializer

__all__ = [
    "EventScheduleListAPIView",
    "EventScheduleDetailAPIView"
]

# Logger initialization
logger = logging.getLogger(__name__)


class EventScheduleListAPIView(APIView):
    """
    Retrieves a list of EventSchedule objects.
    
    GET: Returns all EventSchedule objects in JSON format.
    """
    @swagger_auto_schema(
        operation_summary="Retrieve all events",
        operation_description="Fetches and returns all `EventSchedule` objects in JSON format.",
        responses={
            200: openapi.Response(
                description="List of events",
                schema=EventScheduleSerializer(many=True)
            )
        },
        tags=["Events"]
    )
    def get(self, request) -> Response:
        """
        Retrieves a list of EventSchedule objects.
        
        Args:
            request: Django REST Framework request object.
        
        Returns:
            Response: Response containing event data in JSON format.
        """
        events = EventSchedule.objects.all()
        serializer = EventScheduleSerializer(events, many=True)
        
        logger.info(f"Retrieved {len(events)} event(s) successfully.")
        
        return Response(serializer.data, status=status.HTTP_200_OK)


class EventScheduleDetailAPIView(APIView):
    """
    Retrieves a single EventSchedule object by ID.
    
    GET: Returns a single EventSchedule object based on the provided event_id.
    """
    @swagger_auto_schema(
        operation_summary="Retrieve a single event by ID",
        operation_description="Fetches and returns a single `EventSchedule` object using the provided `event_id`.",
        manual_parameters=[
            openapi.Parameter(
                "event_id",
                openapi.IN_PATH,
                description="ID of the event to retrieve",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={
            200: openapi.Response(
                description="Event details",
                schema=EventScheduleSerializer()
            ),
            404: openapi.Response(
                description="Event not found",
                examples={"application/json": {"detail": "Not found."}}
            )
        },
        tags=["Events"]
    )
    def get(self, request, event_id: int) -> Response:
        """
        Retrieves a single EventSchedule object by ID.
        
        Args:
            request: Django REST Framework request object.
            event_id (int): The ID of the event to be retrieved.
        
        Returns:
            Response: Response containing event data in JSON format.
        """
        event = get_object_or_404(EventSchedule, id=event_id)
        serializer = EventScheduleSerializer(event)
        
        logger.info(f"Event with ID {event_id} retrieved successfully.")
        
        return Response(serializer.data, status=status.HTTP_200_OK)
