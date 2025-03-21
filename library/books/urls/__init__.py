from django.urls import include, path

urlpatterns = [
    path("", include("books.urls.author")),
    path("", include("books.urls.category")),
    path("", include("books.urls.book")),
    path("", include("books.urls.book_review")),
]
