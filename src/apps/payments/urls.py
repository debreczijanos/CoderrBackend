from django.urls import include, path

urlpatterns = [
    path("", include("apps.payments.api.urls")),
]
