from django.urls import path

from .view import ProposalsUpdateView

urlpatterns = [
    path("<int:pk>/", ProposalsUpdateView.as_view(), name="proposals-update"),
]
