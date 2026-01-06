from django.urls import path

from .view import ReviewsUpdateView

urlpatterns = [
    path("<int:pk>/", ReviewsUpdateView.as_view(), name="reviews-update"),
]
