from django.urls import include, path

urlpatterns = [
    path("", include("books.urls.auth")), 
    path("", include("books.urls.author")),
]
