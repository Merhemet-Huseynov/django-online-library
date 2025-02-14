from django.urls import include, path

urlpatterns = [
    path("", include("books.urls.author")),
    path("", include("books.urls.category")),
]
