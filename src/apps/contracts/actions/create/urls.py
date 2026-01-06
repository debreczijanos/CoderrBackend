from django.urls import path

from .view import ContractsCreateView

urlpatterns = [
    path("", ContractsCreateView.as_view(), name="contracts-create"),
]
