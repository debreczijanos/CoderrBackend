from django.urls import path

from .view import ContractsUpdateView

urlpatterns = [
    path("<int:pk>/", ContractsUpdateView.as_view(), name="contracts-update"),
]
