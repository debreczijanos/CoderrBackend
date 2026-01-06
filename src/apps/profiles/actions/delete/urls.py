from django.urls import path

from .view import ProfilesDeleteView

urlpatterns = [
    path("<int:pk>/", ProfilesDeleteView.as_view(), name="profiles-delete"),
]
