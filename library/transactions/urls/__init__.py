from django.urls import include, path

urlpatterns = [
    path("", include("transactions.urls.sale_price_url")),
]
