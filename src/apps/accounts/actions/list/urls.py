from django.urls import path

from .view import AccountsListView

urlpatterns = [
    path("", AccountsListView.as_view(), name="accounts-list"),
]
