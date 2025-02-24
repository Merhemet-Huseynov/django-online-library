import logging
from rest_framework.views import APIView, Response, status
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404

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


class CategoryListViews(APIView):
    """
    View to retrieve a list of all categories.
    
    Allows any user to access the list of categories.
    """
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs) -> Response:
        """
        Retrieve a list of all categories.
        
        Args:
            request: The HTTP request object.
        
        Returns:
            Response: A Response object containing the serialized category data and status code.
        """
        logger.info("Fetching all categories.")
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        logger.info(f"Fetched {len(categories)} categories.")
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryDetailViews(APIView):
    """
    View to retrieve a single category by ID or slug.
    
    Allows any user to access a specific category by its ID or slug.
    """
    permission_classes = [AllowAny]

    def get(self, request, identifier: str, *args, **kwargs) -> Response:
        """
        Retrieve a single category by ID or slug.
        
        Args:
            request: The HTTP request object.
            identifier: The category ID or slug.
        
        Returns:
            Response: A Response object containing the serialized category data and status code.
        """
        logger.info(f"Fetching category with identifier: {identifier}")
        
        if identifier.isdigit():
            category = get_object_or_404(Category, id=identifier)
        else:
            category = get_object_or_404(Category, slug=identifier)
        
        logger.info(f"Fetched category with ID: {category.id} and slug: {category.slug}")
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubCategoryListView(APIView):
    """
    View to find a super category by ID or slug and return its subcategories.
    
    Allows any user to access the subcategories of a specific super category.
    """
    permission_classes = [AllowAny]

    def get(self, request, super_category_name: str, *args, **kwargs) -> Response:
        """
        Finds a super category by ID or slug and returns its subcategories.
        
        Args:
            request: The HTTP request object.
            super_category_name: The super category ID or slug.
        
        Returns:
            Response: A Response object containing the serialized subcategory data and status code.
        """
        if not super_category_name:
            logger.warning("No super category name or ID provided.")
            return Response(
                {"detail": "A super category name or ID is required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        logger.info(f"Fetching super category with identifier: {super_category_name}")
    
        if super_category_name.isdigit():
            super_category = get_object_or_404(
                Category, id=super_category_name
            )
        else:
            super_category = get_object_or_404(
                Category, slug=super_category_name
            )

        subcategories = Category.objects.filter(
            super_category=super_category
        )
        logger.info(
            f"Found {len(subcategories)} subcategories for super category {super_category.name}."
        )
        serializer = SubCategorySerializer(subcategories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)