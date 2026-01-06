from django.urls import path

from .view import ContractsDeleteView

urlpatterns = [
    path("<int:pk>/", ContractsDeleteView.as_view(), name="contracts-delete"),
]
