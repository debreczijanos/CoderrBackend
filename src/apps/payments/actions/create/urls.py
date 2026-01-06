from django.urls import path

from .view import PaymentsCreateView

urlpatterns = [
    path("", PaymentsCreateView.as_view(), name="payments-create"),
]
