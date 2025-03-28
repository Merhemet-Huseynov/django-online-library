from django.urls import path, include
from reservations.views import *

urlpatterns = [
    path(
        "events/", 
        EventScheduleListAPIView.as_view(), 
        name="event-list"
    ),
    path(
        "events/<int:event_id>/", 
        EventScheduleDetailAPIView.as_view(), 
        name="event-detail"
    ),
]