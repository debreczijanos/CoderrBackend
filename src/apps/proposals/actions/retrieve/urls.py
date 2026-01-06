from django.urls import path

from .view import ProposalsRetrieveView

urlpatterns = [
    path("<int:pk>/", ProposalsRetrieveView.as_view(), name="proposals-retrieve"),
]
