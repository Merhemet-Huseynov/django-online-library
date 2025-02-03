from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    # Register endpoints
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
    
    # Author endpoints
    path(
        "authors/",
        AuthorListView.as_view(), 
        name="author-list"
    ),
    path(
        "authors/<int:pk>/",
        AuthorDetailView.as_view(), 
        name="author-detail"
    ),
]