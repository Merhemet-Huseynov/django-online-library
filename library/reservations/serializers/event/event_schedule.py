from rest_framework import serializers
from books.models.event import EventSchedule


class EventScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSchedule
        fields = [
            "id", 
            "name", 
            "description", 
            "start_time", 
            "end_time", 
            "location"
        ]