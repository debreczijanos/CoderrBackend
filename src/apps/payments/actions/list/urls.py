from django.urls import path

from .view import PaymentsListView

urlpatterns = [
    path("", PaymentsListView.as_view(), name="payments-list"),
]
