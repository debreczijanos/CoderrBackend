from django.urls import include, path

urlpatterns = [
    path("", include("apps.projects.api.urls")),
]
