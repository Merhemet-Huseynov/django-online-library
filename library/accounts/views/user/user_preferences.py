import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import get_object_or_404

from accounts.models.user import UserPreferences
from accounts.serializers.user import UserPreferencesDetailSerializer

__all__ = [
    "UserPreferencesAuthenticatedView",
    "UserPreferencesDetailView"
]

# Set up logging
logger = logging.getLogger(__name__)


class UserPreferencesAuthenticatedView(APIView):
    """
    Retrieve the authenticated user's preferences.
    """
    
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve the preferences of the authenticated user.",
        operation_summary="Retrieve Authenticated User Preferences",
        responses={
            200: openapi.Response(
                description="Successfully retrieved user preferences.",
                schema=UserPreferencesDetailSerializer,
                examples={
                    "application/json": {
                        "theme": "dark",
                        "notifications_enabled": True,
                        "language": "en"
                    }
                }
            ),
            404: openapi.Response(
                description="Preferences not found for the authenticated user."
            )
        },
        tags=["User Preferences"]
    )
    def get(self, request, format=None):
        """
        Get the user preferences for the currently authenticated user.
        """
        user_preferences = get_object_or_404(UserPreferences, user=request.user)
        serializer = UserPreferencesDetailSerializer(user_preferences)
        logger.info(f"Retrieved preferences for user: {request.user.id}")
        return Response(serializer.data)


class UserPreferencesDetailView(APIView):
    """
    Retrieve user preferences by user pk.
    """
    
    @swagger_auto_schema(
        operation_description="Retrieve preferences by user pk.",
        operation_summary="Retrieve User Preferences by PK",
        responses={
            200: openapi.Response(
                description="Successfully retrieved user preferences by user pk.",
                schema=UserPreferencesDetailSerializer,
                examples={
                    "application/json": {
                        "theme": "light",
                        "notifications_enabled": False,
                        "language": "fr"
                    }
                }
            ),
            404: openapi.Response(
                description="Preferences not found for the user with the provided pk."
            )
        },
        tags=["User Preferences"]
    )
    def get(self, request, pk, format=None):
        """
        Get the preferences for a user identified by their pk.
        """
        user_preferences = get_object_or_404(UserPreferences, user__pk=pk)
        serializer = UserPreferencesDetailSerializer(user_preferences)
        logger.info(f"Retrieved preferences for user pk: {pk}")
        return Response(serializer.data)
