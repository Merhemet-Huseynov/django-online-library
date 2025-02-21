from django.urls import path
from books.views import *

urlpatterns = [
    # Category endpoints
    path(
        "categories/list/",
        CategoryListView.as_view(),
        name="categories-list"
    ),

    path(
        "categories/detail/<str:identifier>/",
        CategoryDetailView.as_view(),
        name="categories-detail"
    ),

    path(
        "categories/subcategories/<str:super_category_name>/",
        SubCategoryListView.as_view(),
        name="subcategories-list"
    ),
]