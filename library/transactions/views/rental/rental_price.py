import logging
from rest_framework.views import APIView, Response, status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from transactions.models.rental import RentalPrice
from transactions.serializers.rental import RentalPriceSerializer

__all__ = [
    "RentalPriceListAPIView",
    "RentalPriceDetailAPIView"
]

# Set up logging
logger = logging.getLogger(__name__)


class RentalPriceListAPIView(APIView):
    """
    API endpoint that returns a list of all RentalPrice objects.

    This view allows authenticated users to retrieve the list of rental prices for books.
    """
    permission_classes = [AllowAny] 

    @swagger_auto_schema(
        operation_description="This endpoint retrieves the list of all rental prices for books.",
        responses={
            200: RentalPriceSerializer(many=True),
            401: openapi.Response("Unauthorized - Authentication is required"),
            403: openapi.Response("Forbidden - You do not have permission to access this resource"),
        },
        tags=["RentalPrice"],
    )
    def get(self, request):
        """
        Retrieve the list of all rental prices.

        This method is used to fetch the list of all rental prices for books in the system. 
        The response will be a list of rental prices with associated book information.
        """
        rental_prices = RentalPrice.objects.all() 
        serializer = RentalPriceSerializer(rental_prices, many=True)
        logger.info("Successfully retrieved the rental prices list.")
        return Response(serializer.data, status=status.HTTP_200_OK)


class RentalPriceDetailAPIView(APIView):
    """
    API endpoint that returns the details of a specific RentalPrice object based on its primary key.

    This view allows authenticated users to retrieve a specific rental price by its ID (primary key).
    """
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="This endpoint retrieves the details of a specific rental price by its ID (primary key).",
        responses={
            200: RentalPriceSerializer(), 
            400: openapi.Response("Bad Request - Invalid data was provided in the request"), 
            401: openapi.Response("Unauthorized - Authentication is required"), 
            403: openapi.Response("Forbidden - You do not have permission to access this resource"),  
            404: openapi.Response("Not Found - RentalPrice with the specified ID was not found"), 
        },
        tags=["RentalPrice"],
    )
    def get(self, request, pk):
        """
        Retrieve the details of a specific rental price by its primary key.

        This method is used to fetch the rental price for a specific book by its ID (primary key). 
        The response will include the rental price details and the associated book.
        """
        rental_price = get_object_or_404(RentalPrice, pk=pk)
        serializer = RentalPriceSerializer(rental_price)
        logger.info(f"Successfully retrieved rental price details for id {pk}.")
        return Response(serializer.data, status=status.HTTP_200_OK)
