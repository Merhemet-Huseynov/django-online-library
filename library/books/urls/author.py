from django.urls import path
from books.views import *

urlpatterns = [
    # Author endpoints
    path(
        "authors/list/", 
        AuthorListViews.as_view(), 
        name="author-list"
    ),
    
    path(
        "authors/<str:identifier>/", 
        AuthorDetailViews.as_view(), 
        name="author-detail"
    )

]