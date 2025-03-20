from django.urls import path
from books.views import *

urlpatterns = [
    # Author endpoints
    path(
        "authors/", 
        AuthorListViews.as_view(), 
        name="author-list"
    ),
    
    path(
        "authors/<str:identifier>/detail/", 
        AuthorDetailViews.as_view(), 
        name="author-detail"
    )

]