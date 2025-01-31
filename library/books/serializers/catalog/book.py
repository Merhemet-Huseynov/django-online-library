from rest_framework import serializers
from models import Category, Author, Book

class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all()
    )
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )

    class Meta:
        model = Book
        fields = [
            "id", 
            "title", 
            "isbn",
            "published_date", 
            "available", 
            "allow_rental", 
            "book_count", 
            "available_count", 
            "author", 
            "category"
        ]