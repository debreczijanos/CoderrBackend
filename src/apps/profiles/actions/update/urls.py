from django.urls import path

from .view import ProfilesUpdateView

urlpatterns = [
    path("<int:pk>/", ProfilesUpdateView.as_view(), name="profiles-update"),
]
