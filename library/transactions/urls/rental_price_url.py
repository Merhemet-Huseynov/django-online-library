from django.urls import path
from transactions.views import *

urlpatterns = [
    path(
        "rental-prices/", 
        RentalPriceListAPIView.as_view(), 
        name="rental_price_list"
    ),
    path(
        "rental-prices/<int:pk>/detail/", 
        RentalPriceDetailAPIView.as_view(), 
        name="rental_price_detail"
    ),
]
