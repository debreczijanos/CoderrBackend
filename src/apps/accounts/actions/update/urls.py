from django.urls import path

from .view import AccountsUpdateView

urlpatterns = [
    path("<int:pk>/", AccountsUpdateView.as_view(), name="accounts-update"),
]
