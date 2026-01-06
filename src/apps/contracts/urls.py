from django.urls import include, path

urlpatterns = [
    path("", include("apps.contracts.api.urls")),
]
