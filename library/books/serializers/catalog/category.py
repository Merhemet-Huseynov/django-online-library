from rest_framework import serializers
from books.models.catalog import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id", 
            "name", 
            "description"
        ] 