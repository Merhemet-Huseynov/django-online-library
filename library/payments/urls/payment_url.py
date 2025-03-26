from django.urls import path
from payments.views import *

urlpatterns = [
    # Payments endpoints
    path(
        "payments/",
        PaymentListCreateAPIView.as_view(),
        name="payment-list"
    ),
    path(
        "payments/<int:payment_id>/detail/", 
        PaymentDetailAPIView.as_view(), 
        name="payment-detail"
    ),
]