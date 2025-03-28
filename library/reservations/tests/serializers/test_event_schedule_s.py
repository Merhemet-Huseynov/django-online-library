import pytest
from reservations.models.event import EventSchedule
from reservations.serializers.event import EventScheduleSerializer


@pytest.mark.django_db
def test_event_schedule_serializer() -> None:
    """
    Tests the EventScheduleSerializer to ensure it correctly serializes an EventSchedule instance.
    """
    # Create a sample EventSchedule object for testing
    event: EventSchedule = EventSchedule.objects.create(
        name="Test Event",
        description="Test Event Description",
        start_time="2025-03-28 10:00:00+04:00", 
        end_time="2025-03-28 12:00:00+04:00",   
        location="Test Location",
        image="test_image.jpg",
        video="test_video.mp4"
    )
    
    # Serialize the event object
    serializer: EventScheduleSerializer = EventScheduleSerializer(event)
    
    # Validate the serialized data
    assert serializer.data["name"] == "Test Event"
    assert serializer.data["description"] == "Test Event Description"
    assert serializer.data["start_time"] == "2025-03-28T10:00:00+04:00"
    assert serializer.data["end_time"] == "2025-03-28T12:00:00+04:00"
    assert serializer.data["location"] == "Test Location"
