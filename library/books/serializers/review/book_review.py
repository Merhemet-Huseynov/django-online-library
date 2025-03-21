from rest_framework import serializers
from books.models.catalog.book import Book
from books.models.review import BookReview
from django.contrib.auth import get_user_model
from typing import Type

User = get_user_model()


class BookReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for the BookReview model, providing a representation of 
    book reviews with associated book title, user username, and review details.

    Attributes:
        book_title (str): The title of the associated book.
        user_username (str): The username of the user who wrote the review.
        created_at (str): The timestamp when the review was created.

    Meta:
        model (Type[BookReview]): The BookReview model to serialize.
        fields (list): A list of fields to include in the serialized data.
        read_only_fields (list): A list of fields that should be read-only.
    """

    book_title = serializers.CharField(
        source="book.title", 
        read_only=True
    )
    user_username = serializers.CharField(
        source="user.username", 
        read_only=True
    )
    created_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S",  
        read_only=True
    )

    class Meta:
        model = BookReview
        fields = [
            "id", 
            "book", 
            "book_title", 
            "user", 
            "user_username", 
            "rating", 
            "review", 
            "created_at"
        ]
        read_only_fields = [
            "created_at", 
            "book", 
            "user", 
        ]
