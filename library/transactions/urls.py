from django.urls import include, path

urlpatterns = [
    path("transactions", include("transactions.urls")),
]
