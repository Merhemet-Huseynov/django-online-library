from django.urls import path, include
from . import views
from rest_framework.routes import DefaultRouter

router = DefaultRouter()
router.registr(r"books", views.BookViewSet)

urlpatterns = [
    include("api/", include(router.urls)),
]