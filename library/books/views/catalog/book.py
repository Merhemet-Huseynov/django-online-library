import logging
from rest_framework.views import APIView, Response, status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from rest_framework.request import Request

from books.serializers.catalog import BookSerializer
from books.models.catalog import Book

__all__ = [
    "BookListView",
    "BookDetailView"
]

logger = logging.getLogger(__name__)


class BookListView(APIView):
    """
    API endpoint to retrieve a list of all books.
    """
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all books.",
        responses={status.HTTP_200_OK: BookSerializer(many=True)}
    )
    def get(self, request: Request, *args, **kwargs) -> Response:
        """
        Handle GET request to fetch all books.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: A JSON response containing the list of books.
        """
        logger.info("Fetching list of all books.")
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        logger.info(f"Fetched {len(books)} books.")
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookDetailView(APIView):
    """
    API endpoint to retrieve details of a single book by ID or slug.
    """
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a book by ID or slug.",
        responses={status.HTTP_200_OK: BookSerializer()}
    )
    def get(self, request: Request, identifier: str, *args, **kwargs) -> Response:
        """
        Handle GET request to fetch a book by ID or slug.

        Args:
            request (Request): The HTTP request object.
            identifier (str): The book's ID (integer) or slug (string).

        Returns:
            Response: A JSON response containing the book details.
        """
        logger.info(f"Fetching book with identifier: {identifier}")

        if identifier.isdigit():
            book: Book = get_object_or_404(Book, id=int(identifier))
        else:
            book: Book = get_object_or_404(Book, slug=identifier)
        
        logger.info(f"Fetched book with ID: {book.id} and title: {book.title}")
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

