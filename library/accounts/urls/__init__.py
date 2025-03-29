from django.urls import include, path

urlpatterns = [
    path("", include("accounts.urls.auth")),
    path("", include("accounts.urls.password")),
    path("", include("accounts.urls.verfication")),
    path("", include("accounts.urls.user_preferences")),
]
