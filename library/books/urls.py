from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BookViewSet, 
    CategoryViewSet, 
    AuthorViewSet,
    RentalScheduleViewSet, 
    OverdueNotificationViewSet,
    EventScheduleViewSet,
    ReservationScheduleViewSet
)

router = DefaultRouter()
router.register(r"books", BookViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"authors", AuthorViewSet)
router.register(r"rentals", RentalScheduleViewSet)
router.register(r"overdue-notifications", OverdueNotificationViewSet)
router.register(r"events", EventScheduleViewSet) 
router.register(r"reservations", ReservationScheduleViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
