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
    """
    View to list all authors.

    * Allows any user to access the list of authors.
    * Logs the fetching process.
    * Returns a list of authors serialized.
    """
    permission_classes = [AllowAny]

    def get(self, request) -> Response:
        """
        Get the list of all authors.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A Response object with serialized author data.
        """
        logger.info("Fetching all authors.")
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        logger.info(f"Fetched {len(authors)} authors.")
        return Response(serializer.data, status=status.HTTP_200_OK)


class AuthorDetailViews(APIView):
    """
    View to fetch a specific author's details by ID or slug.

    * Allows any user to access author details.
    * Logs the fetching process for the specific author.
    * Returns the author serialized.
    """
    permission_classes = [AllowAny]

    def get(self, request, identifier: str) -> Response:
        """
        Get details of a specific author by ID or slug.

        Args:
            request: The HTTP request object.
            identifier (str): The identifier of the author, either an ID or slug.

        Returns:
            Response: A Response object with serialized author data.
        """
        logger.info(f"Fetching author with identifier: {identifier}")
        if identifier.isdigit():
            author = get_object_or_404(Author, id=identifier)
        else:
            author = get_object_or_404(Author, slug=identifier)

        logger.info(f"Fetched author with ID: {author.id} and slug: {author.slug}")
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)
