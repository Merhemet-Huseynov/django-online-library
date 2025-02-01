from rest_framework import serializers
from books.models.catalog import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            "id", 
            "name", 
            "bio", 
            "birth_date"
        ]