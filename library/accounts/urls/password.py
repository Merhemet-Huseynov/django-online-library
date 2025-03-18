from django.urls import path
from accounts.views import *

urlpatterns = [
    # Password endpoints
    path(
        "accounts/reset-password-send-code/", 
        ResetPasswordSendCodeView.as_view(), 
        name="reset-password-send-code"
    ),

    path(
        "accounts/reset-password/", 
        ResetPasswordView.as_view(), 
        name="reset-password"
    ),
    
    path(
        "accounts/change-password/",
        ChangePasswordView.as_view(), 
        name="change-password"
    ),
]