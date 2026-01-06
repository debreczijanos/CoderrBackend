from django.urls import path

from .view import AccountsLoginView

urlpatterns = [
    path("", AccountsLoginView.as_view(), name="accounts-login"),
]
