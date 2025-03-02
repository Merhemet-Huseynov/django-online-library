from rest_framework import serializers
from transactions.models.rental import RentalSchedule, OverdueFine


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
