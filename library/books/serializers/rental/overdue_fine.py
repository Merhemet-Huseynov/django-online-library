from rest_framework import serializers
from books.models.rental import RentalSchedule, OverdueFine

class OverdueFineSerializer(serializers.ModelSerializer):
    rental = serializers.PrimaryKeyRelatedField(
        queryset=RentalSchedule.objects.all()
    )

    class Meta:
        model = OverdueFine
        fields = [
            "id", 
            "rental", 
            "overdue_days", 
            "fine_amount"
        ]
