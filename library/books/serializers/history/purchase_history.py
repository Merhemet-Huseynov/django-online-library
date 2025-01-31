from rest_framework import serializers
from django.contrib.auth.models import User
from models import Book, PurchaseHistory

class PurchaseHistorySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all()
    )

    class Meta:
        model = PurchaseHistory
        fields = [
            "id", 
            "user", 
            "book", 
            "purchase_date", 
            "sale_price"
        ]
