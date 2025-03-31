from rest_framework import serializers
from transactions.models.rental import OverdueFine


class OverdueFineSerializer(serializers.ModelSerializer):
    """
    Serializer for the OverdueFine model.

    This serializer provides read-only fields for related rental details,
    including the rental ID, book title, and user email.
    """

    rental_id = serializers.IntegerField(
        source="rental.id", 
        read_only=True
    )
    book_title = serializers.CharField(
        source="rental.book.title", 
        read_only=True
    )
    user_email = serializers.EmailField(
        source="rental.user.email", 
        read_only=True
    )

    class Meta:
        model = OverdueFine
        fields = [
            "id", 
            "rental_id", 
            "book_title", 
            "user_email", 
            "overdue_days", 
            "fine_amount"
        ]
