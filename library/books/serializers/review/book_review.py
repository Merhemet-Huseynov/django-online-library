from rest_framework import serializers
from django.contrib.auth.models import User
from books.models.catalog import Book
from books.models.review import BookReview

class BookReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all()
    )

    class Meta:
        model = BookReview
        fields = [
            "id", 
            "book", 
            "user", 
            "rating", 
            "review", 
            "created_at"
        ]
