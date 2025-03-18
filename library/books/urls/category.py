from django.urls import path
from books.views import *

urlpatterns = [
    # Category endpoints
    path(
        "books/categories/list/",
        CategoryListViews.as_view(),
        name="categories-list"
    ),

    path(
        "books/categories/detail/<str:identifier>/",
        CategoryDetailViews.as_view(),
        name="categories-detail"
    ),

    path(
        "books/categories/subcategories/<str:super_category_name>/",
        SubCategoryListView.as_view(),
        name="subcategories-list"
    ),
]