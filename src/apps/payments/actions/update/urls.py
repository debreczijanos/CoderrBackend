from django.urls import path

from .view import PaymentsUpdateView

urlpatterns = [
    path("<int:pk>/", PaymentsUpdateView.as_view(), name="payments-update"),
]
