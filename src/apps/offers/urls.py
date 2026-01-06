from django.urls import include, path

urlpatterns = [
    path("", include("apps.offers.api.urls")),
]
