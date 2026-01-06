from django.urls import path

from .view import ProfilesDetailView

urlpatterns = [
    path("<int:user_id>/", ProfilesDetailView.as_view(), name="profiles-detail"),
]
