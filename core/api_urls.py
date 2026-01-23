from django.urls import include, path

urlpatterns = [
    path("", include("base_info_app.urls")),
    path("", include("accounts_app.urls")),
    path("", include("profiles_app.urls")),
    path("", include("reviews_app.urls")),
    path("", include("offers_app.urls")),
    path("", include("offerdetails_app.urls")),
    path("", include("orders_app.urls")),
]
