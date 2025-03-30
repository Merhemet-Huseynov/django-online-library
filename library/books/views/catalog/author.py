import logging
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from utils.constats import TimeIntervals
from books.models.catalog import Author
from books.serializers.catalog import AuthorSerializer

__all__ = [
    "AuthorListViews",
    "AuthorDetailViews"
]

logger = logging.getLogger(__name__)


@method_decorator(cache_page(TimeIntervals.ONE_MONTH_IN_DAYS), name="dispatch")
class AuthorListViews(APIView):
    """
    View to list all authors.

    * Allows any user to access the list of authors.
    * Logs the fetching process.
    * Returns a list of authors serialized.
    """
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all authors.",
        operation_summary="List all authors",
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="A list of authors",
                schema=AuthorSerializer(many=True),
                examples={
                    "application/json": [
                        {
                            "id": 1,
                            "name": "Author Name",
                            "slug": "author-name",
                            "bio": "Author biography here"
                        },
                        {
                            "id": 2,
                            "name": "Another Author",
                            "slug": "another-author",
                            "bio": "Another author biography here"
                        }
                    ]
                }
            )
        },
        tags=["Authors"]
    )
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


@method_decorator(cache_page(TimeIntervals.ONE_MONTH_IN_DAYS), name="dispatch")
class AuthorDetailViews(APIView):
    """
    View to fetch a specific author's details by ID or slug.

    * Allows any user to access author details.
    * Logs the fetching process for the specific author.
    * Returns the author serialized.
    """
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve details of an author by ID or slug.",
        operation_summary="Retrieve author details",
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Details of the requested author",
                schema=AuthorSerializer(),
                examples={
                    "application/json": {
                        "id": 1,
                        "name": "Author Name",
                        "slug": "author-name",
                        "bio": "Author biography here"
                    }
                }
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Author not found",
                examples={
                    "application/json": {
                        "detail": "Not found."
                    }
                }
            )
        },
        parameters=[
            openapi.Parameter(
                "identifier", 
                openapi.IN_PATH, 
                description="The ID or slug of the author",
                type=openapi.TYPE_STRING
            )
        ],
        tags=["Authors"]  
    )
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
