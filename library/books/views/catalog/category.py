import logging
from rest_framework.views import APIView, Response, status
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from utils.constats import TimeIntervals
from books.models.catalog import Category
from books.serializers.catalog import (
    CategorySerializer, 
    SubCategorySerializer
)

__all__ = [
    "CategoryListViews",
    "CategoryDetailViews",
    "SubCategoryListView"
]

logger = logging.getLogger(__name__)


@method_decorator(cache_page(TimeIntervals.ONE_MONTH_IN_SEC), name="dispatch")
class CategoryListViews(APIView):
    """
    View to retrieve a list of all categories.
    
    Allows any user to access the list of categories.
    """
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all categories.",
        operation_summary="Get All Categories",
        responses={
            status.HTTP_200_OK: CategorySerializer(many=True)
        },
        tags=["Categories"]
    )
    def get(self, request, *args, **kwargs) -> Response:
        """
        Retrieve a list of all categories.
        
        Args:
            request: The HTTP request object.
        
        Returns:
            Response: A Response object containing the serialized category 
            data and status code.
        """
        logger.info("Fetching all categories.")
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        logger.info(f"Fetched {len(categories)} categories.")
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(cache_page(TimeIntervals.ONE_MONTH_IN_SEC), name="dispatch")
class CategoryDetailViews(APIView):
    """
    View to retrieve a single category by ID or slug.
    
    Allows any user to access a specific category by its ID or slug.
    """
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a single category by ID or slug.",
        operation_summary="Get Single Category",
        responses={status.HTTP_200_OK: CategorySerializer()},
        tags=["Categories"]
    )
    def get(self, request, identifier: str, *args, **kwargs) -> Response:
        """
        Retrieve a single category by ID or slug.
        
        Args:
            request: The HTTP request object.
            identifier: The category ID or slug.
        
        Returns:
            Response: A Response object containing the serialized category 
            data and status code.
        """
        logger.info(
            f"Fetching category with identifier: {identifier}"
        )
        
        if identifier.isdigit():
            category = get_object_or_404(
                Category, 
                id=identifier
            )
        else:
            category = get_object_or_404(
                Category, 
                slug=identifier
            )
        
        logger.info(
            f"Fetched category with ID: {category.id} and slug: {category.slug}"
        )
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(cache_page(TimeIntervals.ONE_MONTH_IN_DAYS), name="dispatch")
class SubCategoryListView(APIView):
    """
    View to find a super category by ID or slug and return its subcategories.
    
    Allows any user to access the subcategories of a specific super category.
    """
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve subcategories of a given super category.",
        operation_summary="Get Subcategories of Super Category",
        responses={
            status.HTTP_200_OK: SubCategorySerializer(many=True),
            status.HTTP_400_BAD_REQUEST: openapi.Response("Invalid input"),
        },
        tags=["Categories"]
    )
    def get(self, request, identifier: str, *args, **kwargs) -> Response:
        """
        Finds a super category by ID or slug and returns its subcategories.
        
        Args:
            request: The HTTP request object.
            identifier: The super category ID or slug.
        
        Returns:
            Response: A Response object containing the serialized subcategory data and status code.
        """
        if not identifier:
            logger.warning("No super category name or ID provided.")
            return Response(
                {"detail": "A super category name or ID is required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        logger.info(
            f"Fetching super category with identifier: {identifier}"
        )
    
        if identifier.isdigit():
            super_category = get_object_or_404(
                Category, 
                id=identifier
            )
        else:
            super_category = get_object_or_404(
                Category, 
                slug=identifier
            )

        subcategories = Category.objects.filter(
            super_category=super_category
        )
        logger.info(
            f"Found {len(subcategories)} subcategories for super category {super_category.name}."
        )
        serializer = SubCategorySerializer(subcategories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)