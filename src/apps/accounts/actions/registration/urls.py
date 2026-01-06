from django.urls import path

from .view import AccountsRegistrationView

urlpatterns = [
    path("", AccountsRegistrationView.as_view(), name="accounts-registration"),
]
