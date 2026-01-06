from django.urls import path

from .view import AccountsCreateView

urlpatterns = [
    path("", AccountsCreateView.as_view(), name="accounts-create"),
]
