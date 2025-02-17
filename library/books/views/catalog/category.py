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
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        """Retrieve a list of all categories."""
        logger.info("Fetching all categories.")
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        logger.info(f"Fetched {len(categories)} categories.")
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryDetailViews(APIView):
    permission_classes = [AllowAny]

    def get(self, request, identifier, *args, **kwargs):
        """Retrieve a single category by ID or slug."""
        logger.info(f"Fetching category with identifier: {identifier}")
        
        if identifier.isdigit():
            category = get_object_or_404(Category, id=identifier)
        else:
            category = get_object_or_404(Category, slug=identifier)
        
        logger.info(f"Fetched category with ID: {category.id} and slug: {category.slug}")
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubCategoryListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, super_category_name, *args, **kwargs):
        """
        Finds a super category by ID or slug and returns its subcategories.
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