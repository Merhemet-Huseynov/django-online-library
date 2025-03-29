from django.urls import path, include
from transactions.views import *

urlpatterns = [
    path(
        "sale_price/", 
        SalePriceListAPIView.as_view(), 
        name="sale-price-list"
    ),
    path(
        "sale_price/<int:pk>/",
        SalePriceDetailAPIView.as_view(), 
        name="sale-price-detail"
    ),
]