import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from transactions.models.sale import SalePrice
from transactions.serializers.sale import SalePriceSerializer

__all__ = [
    "SalePriceListAPIView",
    "SalePriceDetailAPIView"
]

# Logger konfiqurasiyası
logger = logging.getLogger(__name__)


class SalePriceListAPIView(APIView):
    """
    API view for listing all sale prices.
    
    Returns a list of all sale prices in the system.
    """
    
    @swagger_auto_schema(
        operation_summary="Get all sale prices",
        operation_description="Retrieve all sale prices available in the system.",
        responses={
            200: openapi.Response(
                description="List of all sale prices",
                schema=SalePriceSerializer(many=True),
                examples={
                    "application/json": [
                        {"id": 1, "price": "100.00", "currency": "USD"},
                        {"id": 2, "price": "150.00", "currency": "EUR"}
                    ]
                }
            )
        },
        tags=["Sale Prices"]
    )
    def get(self, request) -> Response:
        """
        Retrieves all sale prices.

        Returns:
            Response: A Response object containing the list of sale prices.
        """
        sale_prices = SalePrice.objects.all()
        serializer = SalePriceSerializer(sale_prices, many=True)
        logger.info("Fetched all sale prices successfully.")
        return Response(serializer.data)


class SalePriceDetailAPIView(APIView):
    """
    API view for retrieving a single sale price by ID.
    
    Retrieve a sale price by its unique ID (primary key).
    """

    @swagger_auto_schema(
        operation_summary="Get a sale price by ID",
        operation_description="Retrieve a sale price by its primary key.",
        responses={
            200: openapi.Response(
                description="Sale price details",
                schema=SalePriceSerializer,
                examples={
                    "application/json": {
                        "id": 1,
                        "price": "100.00",
                        "currency": "USD"
                    }
                }
            ),
            404: openapi.Response(
                description="Sale price not found",
                examples={
                    "application/json": {"detail": "Not found."}
                }
            )
        },
        tags=["Sale Prices"],
        manual_parameters=[
            openapi.Parameter(
                "pk",
                openapi.IN_PATH,
                description="ID of the sale price to retrieve",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ]
    )
    def get(self, request, pk: int) -> Response:
        """
        Retrieves a sale price by its primary key.

        Args:
            pk (int): The primary key (ID) of the sale price to retrieve.

        Returns:
            Response: A Response object containing the sale price data.
        """
        sale_price = get_object_or_404(SalePrice, pk=pk)
        serializer = SalePriceSerializer(sale_price)
        logger.info(f"Fetched sale price with ID {pk}.")
        return Response(serializer.data)
