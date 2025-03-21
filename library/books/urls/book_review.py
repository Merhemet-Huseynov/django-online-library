from django.urls import path
from books.views.review import *


urlpatterns = [
    # Review endpoints
    path(
        "books/<int:book_id>/reviews/", 
        BookReviewListCreateAPIView.as_view(), 
        name="book-reviews"
    ),
    path(
        "reviews/<int:review_id>/", 
        BookReviewDetailAPIView.as_view(), 
        name="book-review-detail"
    ),
]
