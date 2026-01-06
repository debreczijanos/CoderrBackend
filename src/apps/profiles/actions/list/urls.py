from django.urls import path

from .view import ProfilesListView

urlpatterns = [
    path("", ProfilesListView.as_view(), name="profiles-list"),
]
