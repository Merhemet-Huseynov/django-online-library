from django.urls import path
from transactions.views import *


urlpatterns = [
    # Overdue fine endpoints
    path(
        "overdue_fines/", 
        OverdueFineListView.as_view(),
        name="overdue-fine-list"
    ),
    path(
        "overdue_fines/<int:pk>/",
        OverdueFineDetailView.as_view(), 
        name="overdue-fine-detail"
    ),
]
