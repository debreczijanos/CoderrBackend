from django.urls import path

from .view import ProposalsDeleteView

urlpatterns = [
    path("<int:pk>/", ProposalsDeleteView.as_view(), name="proposals-delete"),
]
