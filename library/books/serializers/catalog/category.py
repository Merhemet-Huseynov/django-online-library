from rest_framework import serializers
from books.models.catalog import Category


class CategorySerializer(serializers.ModelSerializer):
    super_category_name = serializers.SerializerMethodField()
    is_subcategory = serializers.BooleanField(
        read_only=True
    )

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "icon",
            "order",
            "is_active",
            "slug",
            "super_category",
            "super_category_name",
            "is_subcategory"
        ]
        read_only_fields = [
            "slug", 
            "order", 
            "super_category_name",
            "is_subcategory"
        ]

    def get_super_category_name(self, obj):
        return obj.get_super_category_name()