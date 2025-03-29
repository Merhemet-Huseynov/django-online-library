from django.urls import path
from transactions.views import *

urlpatterns = [
    path(
        "sale-transactions/", 
        SaleTransactionListView.as_view(), 
        name="sale-transaction-list"
    ),
    path(
        "sale-transactions/<int:pk>/", 
        SaleTransactionDetailView.as_view(), 
        name="sale-transaction-detail"
    ),
]
