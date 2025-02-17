import logging
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status

from books.models.catalog import Author
from books.serializers.catalog import AuthorSerializer

__all__ = [
    "AuthorListViews", 
    "AuthorDetailViews"
]

logger = logging.getLogger(__name__)


class AuthorListViews(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        logger.info("Fetching all authors.")
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        logger.info(f"Fetched {len(authors)} authors.")
        return Response(serializer.data, status=status.HTTP_200_OK)


class AuthorDetailViews(APIView):
    permission_classes = [AllowAny]

    def get(self, request, identifier):
        logger.info(f"Fetching author with identifier: {identifier}")
        if identifier.isdigit():
            author = get_object_or_404(Author, id=identifier)
        else:
            author = get_object_or_404(Author, slug=identifier)

        logger.info(f"Fetched author with ID: {author.id} and slug: {author.slug}")
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)
