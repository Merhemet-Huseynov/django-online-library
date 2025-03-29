from django.urls import path
from accounts.views import *

urlpatterns = [
    path(
        "preferences/", 
        UserPreferencesAuthenticatedView.as_view(), 
        name="user-preferences-authenticated"
    ),
    path(
        "preferences/<int:pk>/", 
        UserPreferencesDetailView.as_view(), 
        name="user-preferences-detail"
    ),
]
