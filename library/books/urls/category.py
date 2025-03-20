from django.urls import path
from books.views import *

urlpatterns = [
    # Category endpoints
    path(
        "categories/",
        CategoryListViews.as_view(),
        name="categories-list"
    ),

    path(
        "categories/<str:identifier>/detail/",
        CategoryDetailViews.as_view(),
        name="categories-detail"
    ),

    path(
        "subcategories/<str:identifier>/detail",
        SubCategoryListView.as_view(),
        name="subcategories-list"
    ),
]