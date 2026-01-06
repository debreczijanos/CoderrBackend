from django.urls import path

from .view import ContractsRetrieveView

urlpatterns = [
    path("<int:pk>/", ContractsRetrieveView.as_view(), name="contracts-retrieve"),
]
