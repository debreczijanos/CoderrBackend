from django.urls import include, path

urlpatterns = [
    path("", include("apps.profiles.api.urls")),
]
