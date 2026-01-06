from django.urls import path

from .view import AccountsDeleteView

urlpatterns = [
    path("<int:pk>/", AccountsDeleteView.as_view(), name="accounts-delete"),
]
