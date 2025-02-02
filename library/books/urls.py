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
        "register/", 
        RegisterView.as_view(), 
        name="register"
    ),
    path(
        "verify-email/", 
        VerifyEmailView.as_view(),
        name="verify_email"
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