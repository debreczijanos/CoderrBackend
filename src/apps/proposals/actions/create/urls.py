from django.urls import path

from .view import ProposalsCreateView

urlpatterns = [
    path("", ProposalsCreateView.as_view(), name="proposals-create"),
]
