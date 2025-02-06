from django.urls import path
from books.views import *

urlpatterns = [
    # Auth endpoints
    path(
        "send-verification-code/", 
        SendVerificationCodeView.as_view(), 
        name="send_verification_code"
    ),
    path(
        "register/", 
        RegisterView.as_view(),
        name="register"
    ),
    path(
        "login/", 
        LoginView.as_view(), 
        name="login"
    ),
    path(
        "logout/", 
        LogoutView.as_view(), 
        name="logout"
    ),
    path(
        "reset-password-send-code/", 
        ResetPasswordSendCodeView.as_view(), 
        name="reset-password-send-code"
    ),
    path(
        "reset-password/", 
        ResetPasswordView.as_view(), 
        name="reset-password"
    ),
    path(
        "change-password/",
        ChangePasswordView.as_view(), 
        name="change-password"
    ),
]