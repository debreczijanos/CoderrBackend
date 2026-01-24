from django.db.models import Avg
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from offers_app.models import Offer
from profiles_app.models import Profile
from reviews_app.models import Review


class BaseInfoView(APIView):
    """Return aggregated stats for the platform."""
    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request):
        """Return review, profile, and offer counts."""
        review_stats = Review.objects.aggregate(avg_rating=Avg("rating"))
        average_rating = review_stats["avg_rating"] or 0
        return Response(
            {
                "review_count": Review.objects.count(),
                "average_rating": round(average_rating, 1),
                "business_profile_count": Profile.objects.filter(
                    type=Profile.TYPE_BUSINESS
                ).count(),
                "offer_count": Offer.objects.count(),
            }
        )
