from rest_framework import serializers
from django.contrib.auth.models import User

from books.models.catalog import Book
from transactions.models.history import RentalHistory


class RentalHistorySerializer(serializers.ModelSerializer):
    """
    Serializer for the RentalHistory model.
    This serializer allows rental history data to be represented in JSON format.
    """

    user = serializers.StringRelatedField()  
    book = serializers.StringRelatedField() 

    class Meta:
        model = RentalHistory  
        fields = [
            "id",                 
            "user",               
            "book",              
            "rental_start_date",  
            "rental_end_date",    
            "rental_duration",    
            "rental_price",       
        ]
