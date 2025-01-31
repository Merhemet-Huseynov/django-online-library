from rest_framework import serializers
from django.contrib.auth.models import User
from models import Book, BookRecommendation

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
