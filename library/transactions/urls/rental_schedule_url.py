from django.urls import path
from transactions.views import *


urlpatterns = [
    path(
        "rental-schedules/", 
        RentalScheduleListCreateAPIView.as_view(), 
        name="rental-schedule-list-create"
    ),
    path(
        "rental-schedules/<int:pk>/detail", 
        RentalScheduleDetailAPIView.as_view(), 
        name="rental-schedule-detail"
    ),
]
