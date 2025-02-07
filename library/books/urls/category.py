from django.urls import path
from books.views import *

urlpatterns = [
    path(
        "categories/", 
        CategoryListView.as_view(), 
        name="category-list"
    ), 
    path(
        "categories/<int:parent_id>/subcategories/", 
        SubCategoryListView.as_view(), 
        name="subcategory-list"
    ),
]
