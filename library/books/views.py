from rest_framework import viewsets
from .models import (
    Book, 
    Category, 
    Author, 
    RentalSchedule, 
    OverdueNotification, 
    EventSchedule, 
    ReservationSchedule
)
from .serializers import (
    BookSerializer, 
    CategorySerializer, 
    AuthorSerializer, 
    RentalScheduleSerializer, 
    OverdueNotificationSerializer, 
    EventScheduleSerializer, 
    ReservationScheduleSerializer
)


# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Author ViewSet
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# Book ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# RentalSchedule ViewSet
class RentalScheduleViewSet(viewsets.ModelViewSet):
    queryset = RentalSchedule.objects.all()
    serializer_class = RentalScheduleSerializer


# OverdueNotification ViewSet
class OverdueNotificationViewSet(viewsets.ModelViewSet):
    queryset = OverdueNotification.objects.all()
    serializer_class = OverdueNotificationSerializer


# EventSchedule ViewSet
class EventScheduleViewSet(viewsets.ModelViewSet):
    queryset = EventSchedule.objects.all()
    serializer_class = EventScheduleSerializer


# ReservationSchedule ViewSet
class ReservationScheduleViewSet(viewsets.ModelViewSet):
    queryset = ReservationSchedule.objects.all()
    serializer_class = ReservationScheduleSerializer