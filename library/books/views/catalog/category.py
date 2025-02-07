from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from books.models.catalog import Category
from books.serializers.catalog.category import CategorySerializer

__all__ = ["CategoryListView", "SubCategoryListView"]

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.filter(parent__isnull=True)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SubCategoryListView(APIView):
    def get(self, request, parent_id):
        try:
            parent_category = Category.objects.get(id=parent_id)
            subcategories = Category.objects.filter(parent=parent_category)
            serializer = CategorySerializer(subcategories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({
                "error": "Parent category not found"
                }, status=status.HTTP_404_NOT_FOUND
            )