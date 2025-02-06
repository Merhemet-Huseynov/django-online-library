from django.urls import include, path

urlpatterns = [
    path("books/", include("books.urls")),
]