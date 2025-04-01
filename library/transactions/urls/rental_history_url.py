from django.urls import path
from transactions.views.history import *

urlpatterns = [
    path(
        "rental-history/", 
        RentalHistoryListView.as_view(), 
        name="rental-history-list"
    ),
    path(
        "rental-history/<int:pk>/", 
        RentalHistoryDetailView.as_view(), 
        name="rental-history-detail"
    ),
]
