from django.urls import path

from .view import ProfilesCreateView

urlpatterns = [
    path("", ProfilesCreateView.as_view(), name="profiles-create"),
]
