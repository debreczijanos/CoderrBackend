from django.urls import path

from .view import ProfilesRetrieveView

urlpatterns = [
    path("<int:pk>/", ProfilesRetrieveView.as_view(), name="profiles-retrieve"),
]
