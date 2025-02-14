from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status

from books.models.catalog import Author
from books.serializers.catalog import AuthorSerializer


__all__ = [
    "AuthorListViews", 
    "AuthorDetailViews" 
]


class AuthorListViews(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AuthorDetailViews(APIView):
    permission_classes = [AllowAny]

    def get(self, request, identifier):
        if identifier.isdigit(): 
            author = get_object_or_404(Author, id=identifier)
        else:
            author = get_object_or_404(Author, slug=identifier)

        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)