from django.urls import include, path

urlpatterns = [
    path("", include("event_manager.urls.event_schedule")),
]
