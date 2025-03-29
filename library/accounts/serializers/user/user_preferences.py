from rest_framework import serializers
from django.contrib.auth.models import User

from accounts.models.user import UserPreferences
from books.models.catalog import Book, Category, Author
from books.models.review import BookRecommendation


class UserPreferencesSerializer(serializers.ModelSerializer):
    """
    Serializer for user preferences, allowing users to specify their favorite categories and authors.
    """
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    favorite_categories = serializers.SerializerMethodField()
    favorite_authors = serializers.SerializerMethodField()
    
    class Meta:
        model = UserPreferences
        fields = [
            "user", 
            "favorite_categories", 
            "favorite_authors"
        ]
        ref_name = "UserPreferencesSerializer"

    def get_favorite_categories(self, obj):
        """Return category names instead of IDs."""
        return [category.name for category in obj.favorite_categories.all()]

    def get_favorite_authors(self, obj):
        """Return author names instead of IDs."""
        return [author.name for author in obj.favorite_authors.all()]


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model, providing all available fields.
    """
    class Meta:
        model = Book
        fields = "__all__"
        ref_name = "BookSerializer"


class BookRecommendationSerializer(serializers.ModelSerializer):
    """
    Serializer for book recommendations, including user and the recommended book.
    """
    book = BookSerializer()

    class Meta:
        model = BookRecommendation
        fields = [
            "user", 
            "book"
        ]
        ref_name = "BookRecommendationSerializer"


class UserPreferencesDetailSerializer(UserPreferencesSerializer):
    """
    Detailed serializer for user preferences, including recommended books
    based on the user's top-rated books, popular books, and books by favorite authors.
    """
    top_rated_books = BookSerializer(many=True, read_only=True)
    popular_books = BookSerializer(many=True, read_only=True)
    books_by_favorite_authors = BookSerializer(many=True, read_only=True)

    class Meta(UserPreferencesSerializer.Meta):
        fields = UserPreferencesSerializer.Meta.fields + ["top_rated_books", 
                                                          "popular_books", 
                                                          "books_by_favorite_authors"]
        ref_name = "UserPreferencesDetailSerializer"
