from django.urls import path

from .view import PaymentsDeleteView

urlpatterns = [
    path("<int:pk>/", PaymentsDeleteView.as_view(), name="payments-delete"),
]
