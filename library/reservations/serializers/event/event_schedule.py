from rest_framework import serializers
from reservations.models.event import EventSchedule


class EventScheduleSerializer(serializers.ModelSerializer):
    """
    Serializer for EventSchedule model, to serialize event schedule data.
    """
    class Meta:
        model = EventSchedule
        fields = [
            "id", 
            "name", 
            "description", 
            "start_time", 
            "end_time", 
            "location",
            "image",
            "video"
        ]