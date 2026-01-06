from django.urls import include, path

urlpatterns = [
    path("", include("apps.proposals.api.urls")),
]
