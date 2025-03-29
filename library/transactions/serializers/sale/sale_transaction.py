from rest_framework import serializers
from transactions.models.sale import SaleTransaction
from books.models import Book
from transactions.models.history import PurchaseHistory
from django.contrib.auth import get_user_model

User = get_user_model()


class SaleTransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for the SaleTransaction model, which represents a sale transaction
    involving a user, a book, a sale price, and a sale date.
    It provides methods for creating and updating SaleTransaction instances.
    """
    
    user = serializers.StringRelatedField()  
    book = serializers.StringRelatedField()
    sale_date = serializers.DateField()
    status = serializers.ChoiceField(choices=SaleTransaction.STATUS_CHOICES)
    sale_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    
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

    def create(self, validated_data):
        """
        Creates a new SaleTransaction instance from the validated data.
        
        Args:
            validated_data (dict): The data validated by the serializer.
        
        Returns:
            SaleTransaction: The newly created SaleTransaction instance.
        """
        sale_transaction = SaleTransaction(**validated_data)
        sale_transaction.save()
        return sale_transaction

    def update(self, instance, validated_data):
        """
        Updates an existing SaleTransaction instance with the provided data.
        
        Args:
            instance (SaleTransaction): The instance to update.
            validated_data (dict): The validated data to update the instance with.
        
        Returns:
            SaleTransaction: The updated SaleTransaction instance.
        """
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
