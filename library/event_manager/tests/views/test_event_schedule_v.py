import pytest
from rest_framework import status
from django.urls import reverse
from event_manager.models.event import EventSchedule
from django.utils import timezone


@pytest.mark.django_db
def test_event_schedule_list_view(client):
    """
    Test for the EventScheduleListAPIView which retrieves all events.
    """
    # Create some event schedules to be fetched by the API
    start_time = timezone.now()
    end_time = start_time + timezone.timedelta(hours=2)
    
    event1 = EventSchedule.objects.create(
        name="Event 1",
        location="Location 1",
        description="Description 1",
        start_time=start_time,
        end_time=end_time
    )
    
    event2 = EventSchedule.objects.create(
        name="Event 2",
        location="Location 2",
        description="Description 2",
        start_time=start_time,
        end_time=end_time
    )
    
    # Define the URL for the event list API endpoint
    url = reverse("event-list")
    
    # Make the GET request to the API
    response = client.get(url)
    
    # Check if the status code is OK
    assert response.status_code == status.HTTP_200_OK
    
    # Check if the response contains the serialized data of both events
    assert len(response.data) == 2  
    assert response.data[0]["name"] == event1.name
    assert response.data[1]["name"] == event2.name


@pytest.mark.django_db
def test_event_schedule_detail_view(client):
    """
    Test for the EventScheduleDetailAPIView which retrieves a single event by ID.
    """
    # Create an event schedule to be fetched by the API
    start_time = timezone.now()
    end_time = start_time + timezone.timedelta(hours=2)
    
    event = EventSchedule.objects.create(
        name="Test Event",
        location="Test Location",
        description="Test Description",
        start_time=start_time,
        end_time=end_time
    )
    
    # Define the URL for the event detail API endpoint
    url = reverse("event-detail", kwargs={"event_id": event.id})
    
    # Make the GET request to the API
    response = client.get(url)
    
    # Check if the status code is OK
    assert response.status_code == status.HTTP_200_OK
    
    # Check if the response contains the serialized data of the event
    assert response.data["name"] == event.name
    assert response.data["location"] == event.location
    assert response.data["description"] == event.description


@pytest.mark.django_db
def test_event_schedule_detail_view_not_found(client):
    """
    Test for the EventScheduleDetailAPIView with a non-existing event ID.
    """
    # Define a non-existing event ID
    non_existing_event_id = 999
    
    # Define the URL for the event detail API endpoint
    url = reverse("event-detail", kwargs={"event_id": non_existing_event_id})
    
    # Make the GET request to the API
    response = client.get(url)
    
    # Check if the status code is 404 (Not Found)
    assert response.status_code == status.HTTP_404_NOT_FOUND
