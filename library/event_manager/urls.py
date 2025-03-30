from django.urls import include, path

urlpatterns = [
    path("event_manager/", include("event_manager.urls")),
]