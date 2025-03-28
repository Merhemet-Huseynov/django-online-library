from django.urls import include, path

urlpatterns = [
    path("", include("reservations.urls.event_schedule")),
]
