from django.urls import path
from transactions.views.history import *

urlpatterns = [
    path(
        "purchase-history/", 
        PurchaseHistoryListView.as_view(), 
        name="purchase-history-list"
    ),
    path(
        "purchase-history/<int:pk>/", 
        PurchaseHistoryDetailView.as_view(), 
        name="purchase-history-detail"
    ),
]