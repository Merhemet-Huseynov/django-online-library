from django.urls import path
from accounts.views import *

urlpatterns = [
    # Verfication endpoints
    path(
        "accounts/send-verification-code/", 
        SendVerificationCodeView.as_view(), 
        name="send_verification_code"
    ),
]