from rest_framework import serializers
from django.contrib.auth.models import User

from books.models.catalog import Book
from books.models.review import BookRecommendation


class BookRecommendationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    book = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )

    class Meta:
        model = BookRecommendation
        fields = [
            "id", 
            "user", 
            "book", 
            "recommended_on"
        ]
