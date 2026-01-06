from django.urls import path

from .view import ReviewsDetailView

urlpatterns = [
    path("<int:review_id>/", ReviewsDetailView.as_view(), name="reviews-detail"),
]
