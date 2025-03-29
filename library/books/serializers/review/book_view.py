from rest_framework import serializers
from django.contrib.auth.models import User

from books.models.catalog import Book
from books.models.review import UserBookView, BookRecommendation


class UserBookViewSerializer(serializers.ModelSerializer):
    """
    Serializer for the `UserBookView` model, used to convert the model instance 
    into JSON format and vice versa for API interaction.

    Fields:
    - `user`: A read-only field that returns the username of the user who viewed 
      the book.
    - `book`: A read-only field that returns the title of the book viewed by the user.
    - `viewed_on`: A `DateTimeField` that formats the timestamp of when the book 
      was viewed.

    The `StringRelatedField` is used to display the string representation of related 
    fields.
    """
    user = serializers.StringRelatedField(read_only=True) 
    book = serializers.StringRelatedField(read_only=True) 
    viewed_on = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S") 

    class Meta:
        model = UserBookView
        fields = [
            "id",
            "user",       
            "book",       
            "viewed_on"   
        ]