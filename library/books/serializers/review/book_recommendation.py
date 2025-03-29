from rest_framework import serializers
from books.models import BookRecommendation
from books.models import Book
from django.contrib.auth.models import User


class BookRecommendationSerializer(serializers.ModelSerializer):
    """
    Serializer for the `BookRecommendation` model. It is used to convert 
    the model instance into a JSON representation and vice versa.

    Fields:
    - `user`: A read-only field that returns the username of the user 
      associated with the recommendation.
    - `book`: A read-only field that returns the title of the book being 
      recommended.
    - `recommended_on`: The date the recommendation was made.

    The `StringRelatedField` is used to display the string representation 
    of related fields.
    """
    user = serializers.StringRelatedField(read_only=True)  
    book = serializers.StringRelatedField(read_only=True) 

    class Meta:
        model = BookRecommendation
        fields = [
            "id",        
            "user",      
            "book",       
            "recommended_on"  
        ]
