from django.urls import include, path

urlpatterns = [
    path("reservations/", include("reservations.urls")),
]