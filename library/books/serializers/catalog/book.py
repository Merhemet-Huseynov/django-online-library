from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer
from books.models.catalog import Category, Author, Book


class BookSerializer(TaggitSerializer, serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all()
    )
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), 
        required=False, 
        allow_null=True
    )
    tags = TagListSerializerField(
        required=False
    )

    class Meta:
        model = Book
        fields = [
            # Basic Book Information
            "id",
            "title",
            "isbn",
            "description",
            "published_date",
            "slug",

            # Book Properties
            "condition",
            "book_format",
            "page_count",
            "edition",
            "publisher",
            "language",
            "shelf_location",

            # Physical and Digital Features
            "image",
            "digital_file",

            # Relationships and Features
            "tags",
            "allow_rental",
            "available",
            "book_count",
            "available_count",
            "added_date",
            "author",
            "category"
        ]

        read_only_fields = ["added_date"]

    def validate_isbn(self, value):
        if value and len(value) not in [10, 13]:
            raise serializers.ValidationError(
                "ISBN must be 10 or 13 digits."
            )
        return value

    def validate(self, attrs):
        """
        Ensures that if the book format is "ebook", a digital file 
        must be provided.
        """
        if attrs.get("book_format") == "ebook" and not attrs.get("digital_file"):
            raise serializers.ValidationError(
                "An E-Book file must be provided for E-Book format."
            )
        return attrs
