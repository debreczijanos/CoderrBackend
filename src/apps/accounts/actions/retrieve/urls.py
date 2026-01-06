from django.urls import path

from .view import AccountsRetrieveView

urlpatterns = [
    path("<int:pk>/", AccountsRetrieveView.as_view(), name="accounts-retrieve"),
]
