from django.urls import path
from books.views import *


urlpatterns = [
    # Book endpoints
    path(
        "books/",
        BookListView.as_view(),
        name="book-list"
    ),
    path(
        "books/<str:identifier>/detail",
        BookDetailView.as_view(),
        name="book-detail"
    )    
]
