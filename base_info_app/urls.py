from django.urls import include, path

from . import views

urlpatterns = [
    path("health/", views.health, name="health"),
    path("", include("base_info_app.api.urls")),
]
