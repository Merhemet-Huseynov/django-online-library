from django.urls import path
from books.views import *

urlpatterns = [
    # Author endpoints
    path(
        "books/authors/list/", 
        AuthorListViews.as_view(), 
        name="author-list"
    ),
    
    path(
        "books/authors/<str:identifier>/", 
        AuthorDetailViews.as_view(), 
        name="author-detail"
    )

]