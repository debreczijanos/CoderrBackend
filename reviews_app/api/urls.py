from django.urls import path

from .views import ReviewDetailView, ReviewsCollectionView

urlpatterns = [
    path("reviews/", ReviewsCollectionView.as_view(), name="reviews-collection"),
    path("reviews/<int:review_id>/", ReviewDetailView.as_view(), name="reviews-detail"),
]
