from django.urls import include, path

urlpatterns = [
    path("", include("offerdetails_app.api.urls")),
]
