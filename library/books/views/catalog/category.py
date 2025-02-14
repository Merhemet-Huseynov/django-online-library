from rest_framework.views import APIView, Response, status
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404

from books.serializers.catalog import CategorySerializer
from books.models.catalog import Category

__all__ = [
    "CategoryListViews",
    "CategoryDetailViews"
]


class CategoryListViews(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryDetailViews(APIView):
    permission_classes = [AllowAny]

    def get(self, request, identifier, *args, **kwargs):
        if identifier.isdigit():
            category = get_object_or_404(Category, id=identifier)
        else:
            category = get_object_or_404(Category, slug=identifier)
        
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)