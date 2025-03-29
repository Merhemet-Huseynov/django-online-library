from django.urls import path
from books.views import *

urlpatterns = [
    # Book recomendations
    path(
        "recommendations/", 
        BookRecommendationListView.as_view(), 
        name="book-recommendations"
    ),
    path(
        "recommendations/<int:pk>/", 
        BookRecommendationDetailView.as_view(), 
        name="book-recommendations"
    ),
]
