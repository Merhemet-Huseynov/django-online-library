import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404 
from drf_yasg.utils import swagger_auto_schema

from books.models.review import BookRecommendation
from books.serializers.review import BookRecommendationSerializer

__all__ = [
    "BookRecommendationListView",
    "BookRecommendationDetailView"
]

# Logging conf
logger = logging.getLogger(__name__)


class BookRecommendationListView(APIView):
    """
    API view to retrieve book recommendations for the authenticated user.
    
    This view allows an authenticated user to get a list of all book 
    recommendations that are associated with their user profile.
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve book recommendations for the authenticated user",
        responses={200: BookRecommendationSerializer(many=True)}
    )
    def get(self, request):
        """
        Retrieves the list of book recommendations for the authenticated user.

        Args:
            request: The HTTP request object containing the user's information.

        Returns:
            Response: A list of book recommendations for the authenticated user.
        """
        recommendations = BookRecommendation.objects.filter(user=request.user)
        serializer = BookRecommendationSerializer(recommendations, many=True)
        logger.info(f"Successfully fetched {len(recommendations)} recommendations for user {request.user.id}.")
        return Response(serializer.data)


class BookRecommendationDetailView(APIView):
    """
    API view to retrieve a specific book recommendation for the authenticated user.

    This view allows an authenticated user to get a single book recommendation 
    by its primary key (ID) if it belongs to them.
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve a specific book recommendation for the authenticated user",
        responses={200: BookRecommendationSerializer, 404: "Recommendation not found"}
    )
    def get(self, request, pk):
        """
        Retrieves a specific book recommendation for the authenticated user.

        Args:
            request: The HTTP request object containing the user's information.
            pk: The primary key of the recommendation.

        Returns:
            Response: A detailed book recommendation if found, or an error message if not found.
        """
        recommendation = get_object_or_404(BookRecommendation, id=pk, user=request.user)
        serializer = BookRecommendationSerializer(recommendation)
        logger.info(f"Successfully fetched recommendation with ID {pk} for user {request.user.id}.")
        return Response(serializer.data)