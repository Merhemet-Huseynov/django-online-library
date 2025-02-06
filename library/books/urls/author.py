from django.urls import path
from books.views import *

urlpatterns = [
    # Author endpoints
    path(
        "authors/list/", 
        AuthorListView.as_view(), 
        name="author-list"
    ),
    path(
        "author/create/", 
        AuthorCreateView.as_view(), 
        name="author-create"
    ),
    path(
        "author/detail/<int:pk>/", 
        AuthorDetailView.as_view(), 
        name="author-detail"
    ),
    path(
        "author/update/<int:pk>/", 
        AuthorUpdateView.as_view(), 
        name="author-update"
    ),
    path(
        "author/delete/<int:pk>/", 
        AuthorDeleteView.as_view(), 
        name="author-delete"
    ),
]