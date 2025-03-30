from django.urls import include, path

urlpatterns = [
    path("", include("transactions.urls.sale_price_url")),
    path("", include("transactions.urls.sale_transaction_url")),
    path("", include("transactions.urls.rental_price_url")),
]
