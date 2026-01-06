from django.urls import path

from .view import PaymentsRetrieveView

urlpatterns = [
    path("<int:pk>/", PaymentsRetrieveView.as_view(), name="payments-retrieve"),
]
