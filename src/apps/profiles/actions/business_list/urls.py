from django.urls import path

from .view import ProfilesBusinessListView

urlpatterns = [
    path("business/", ProfilesBusinessListView.as_view(), name="profiles-business-list"),
]
