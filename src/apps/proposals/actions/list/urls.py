from django.urls import path

from .view import ProposalsListView

urlpatterns = [
    path("", ProposalsListView.as_view(), name="proposals-list"),
]
