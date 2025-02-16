from rest_framework import serializers
from books.models.catalog import Category

class CategorySerializer(serializers.ModelSerializer):
    # Təyin edilmiş super kateqoriya və onun adı (əgər varsa)
    super_category_name = serializers.CharField(
        source='get_super_category_name', read_only=True
    )
    
    class Meta:
        model = Category
        fields = (
            'id', 
            'name', 
            'slug', 
            'icon', 
            'order', 
            'is_active', 
            'super_category', 
            'super_category_name'
        )

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 
            'name', 
            'slug', 
            'icon', 
            'order', 
            'is_active', 
            'super_category'
        )
        extra_kwargs = {
            'super_category': {'required': True}  # Sub kateqoriyalar üçün super kateqoriya tələb olunur
        }
