from django.urls import path
from books.views import *

urlpatterns = [
    path(
        "categories/list",
        CategoryListViews.as_view(),
        name="categories-list"
    ),
    path(
        "categories/detail/<str:identifier>/",
        CategoryDetailViews.as_view(),
        name="categories/detail/"
    )    
]