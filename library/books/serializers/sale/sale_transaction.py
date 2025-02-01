from rest_framework import serializers
from django.contrib.auth.models import User
from books.models.catalog import Book
from books.models.sale import SaleTransaction

class SaleTransactionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all()
    )

    class Meta:
        model = SaleTransaction
        fields = [
            "id", 
            "user", 
            "book", 
            "sale_price", 
            "sale_date", 
            "status"
        ]
