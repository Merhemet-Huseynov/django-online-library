import logging
from typing import Any
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView, Response, status
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from books.models.review import BookReview
from books.models.catalog.book import Book
from books.serializers.review import BookReviewSerializer

__all__ = [
    "BookReviewListCreateAPIView",
    "BookReviewDetailAPIView",
]

logger = logging.getLogger(__name__)


class BookReviewListCreateAPIView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_description="Retrieve all reviews for a given book.",
        operation_summary="Get Book Reviews",
        responses={200: BookReviewSerializer(many=True)},
        tags=["Book Reviews"]
    )
    def get(self, request: Any, book_id: int) -> Response:
        """
        Retrieve all reviews for a given book.
        
        Args:
            request (Any): The HTTP request object.
            book_id (int): The ID of the book.
        
        Returns:
            Response: A JSON response containing a list of reviews for the specified book.
        """
        book = get_object_or_404(Book, id=book_id)
        reviews = BookReview.objects.filter(book=book)
        serializer = BookReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new review for a specified book.",
        operation_summary="Create Book Review",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "rating": openapi.Schema(type=openapi.TYPE_INTEGER, description="Rating of the book (1-5)"),
                "review": openapi.Schema(type=openapi.TYPE_STRING, description="The text content of the review")
            },
            required=["rating", "review"]
        ),
        responses={201: BookReviewSerializer(), 400: "Bad Request"},
        tags=["Book Reviews"]
    )
    def post(self, request: Any, book_id: int) -> Response:
        """
        Create a new review for a specified book.
        
        Args:
            request (Any): The HTTP request object containing review data.
            book_id (int): The ID of the book being reviewed.
        
        Returns:
            Response: A JSON response containing the created review data.
        """
        book = get_object_or_404(Book, id=book_id)
        serializer = BookReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(book=book, user=request.user)
            logger.info(f"New review created by user {request.user} for book {book_id}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        logger.warning("Review creation failed", extra={"errors": serializer.errors})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookReviewDetailAPIView(APIView):
    """
    API endpoint to retrieve, update, or delete a specific book review.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, review_id: int) -> BookReview:
        """
        Retrieve a review object by its ID.
        
        Args:
            review_id (int): The ID of the review.
        
        Returns:
            BookReview: The requested review object.
        """
        return get_object_or_404(BookReview, id=review_id)

    @swagger_auto_schema(
        operation_description="Retrieve details of a specific review.",
        operation_summary="Get Book Review Details",
        responses={200: BookReviewSerializer(), 404: "Not Found"},
        tags=["Book Reviews"]
    )
    def get(self, request: Any, review_id: int) -> Response:
        """
        Retrieve details of a specific review.
        
        Args:
            request (Any): The HTTP request object.
            review_id (int): The ID of the review.
        
        Returns:
            Response: A JSON response containing the review details.
        """
        review = self.get_object(review_id)
        serializer = BookReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Update an existing review if the requesting user is the owner.",
        operation_summary="Update Book Review",
        request_body=BookReviewSerializer,
        responses={200: BookReviewSerializer(), 400: "Bad Request", 403: "Forbidden"},
        tags=["Book Reviews"]
    )
    def put(self, request: Any, review_id: int) -> Response:
        """
        Update an existing review if the requesting user is the owner.
        
        Args:
            request (Any): The HTTP request object containing updated review data.
            review_id (int): The ID of the review.
        
        Returns:
            Response: A JSON response containing the updated review data.
        """
        review = self.get_object(review_id)
        if review.user != request.user:
            logger.warning(f"Unauthorized review edit attempt by user {request.user}")
            return Response(
                {"error": "You can only edit your own reviews."}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = BookReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a review if the requesting user is the owner.",
        operation_summary="Delete Book Review",
        responses={204: "No Content", 403: "Forbidden"},
        tags=["Book Reviews"]
    )
    def delete(self, request: Any, review_id: int) -> Response:
        """
        Delete a review if the requesting user is the owner.
        
        Args:
            request (Any): The HTTP request object.
            review_id (int): The ID of the review to be deleted.
        
        Returns:
            Response: A JSON response indicating the deletion status.
        """
        review = self.get_object(review_id)
        if review.user != request.user:
            logger.warning(f"Unauthorized review delete attempt by user {request.user}")
            return Response(
                {"error": "You can only delete your own reviews."}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        review.delete()
        logger.info(f"Review {review_id} deleted by user {request.user}")
        return Response({"message": "Review deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
