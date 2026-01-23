from django.urls import include, path

urlpatterns = [
    path("", include("accounts_app.api.urls")),
]
