from rest_framework import serializers
from books.models.catalog import Author


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Converts Author model instances to JSON format and vice versa.
    """
    
    class Meta:
        
        model: type[Author] = Author
        fields: list[str] = [
            "id", 
            "name", 
            "bio", 
            "birth_date",
            "image",
            "slug"
        ]
