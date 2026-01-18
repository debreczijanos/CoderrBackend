from django.db.models import Avg
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.offers.models import Offer
from apps.profiles.models import Profile
from apps.reviews.models import Review


@api_view(["GET"])
@authentication_classes([])
@permission_classes([AllowAny])
def base_info(request):
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
