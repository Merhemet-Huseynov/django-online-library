from rest_framework import serializers
from books.models.user import UserPreferences
from books.models.catalog import Category, Author


class UserPreferencesSerializer(serializers.ModelSerializer):
    favorite_categories = serializers.StringRelatedField(
        many=True
    )
    favorite_authors = serializers.StringRelatedField(
        many=True
    )

    class Meta:
        model = UserPreferences
        fields = [
            "id", 
            "favorite_categories", 
            "favorite_authors"
        ]
