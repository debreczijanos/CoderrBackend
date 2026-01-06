from django.urls import path

from .view import ContractsListView

urlpatterns = [
    path("", ContractsListView.as_view(), name="contracts-list"),
]
