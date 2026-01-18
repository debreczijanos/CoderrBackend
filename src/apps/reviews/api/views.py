from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.profiles.models import Profile
from apps.reviews.api.serializers import (
    ReviewCreateSerializer,
    ReviewSerializer,
    ReviewUpdateSerializer,
)
from apps.reviews.models import Review


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def reviews_collection(request):
    if request.method == "GET":
        queryset = Review.objects.all()
        business_user_id = request.query_params.get("business_user_id")
        if business_user_id:
            if not business_user_id.isdigit():
                return Response(
                    {"detail": "business_user_id must be an integer."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            queryset = queryset.filter(business_user_id=int(business_user_id))

        reviewer_id = request.query_params.get("reviewer_id")
        if reviewer_id:
            if not reviewer_id.isdigit():
                return Response(
                    {"detail": "reviewer_id must be an integer."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            queryset = queryset.filter(reviewer_id=int(reviewer_id))

        ordering = request.query_params.get("ordering")
        if ordering in {"updated_at", "-updated_at", "rating", "-rating"}:
            queryset = queryset.order_by(ordering)

        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    profile = Profile.objects.filter(user=request.user).first()
    if not profile or profile.type != Profile.TYPE_CUSTOMER:
        return Response(
            {"detail": "Only customers can create reviews."},
            status=status.HTTP_403_FORBIDDEN,
        )

    serializer = ReviewCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    business_user_id = serializer.validated_data["business_user"]
    business_profile = Profile.objects.filter(user_id=business_user_id).first()
    if not business_profile or business_profile.type != Profile.TYPE_BUSINESS:
        return Response(
            {"detail": "Business user not found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    if Review.objects.filter(
        business_user_id=business_user_id, reviewer=request.user
    ).exists():
        return Response(
            {"detail": "You have already reviewed this business user."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    review = Review.objects.create(
        business_user_id=business_user_id,
        reviewer=request.user,
        rating=serializer.validated_data["rating"],
        description=serializer.validated_data["description"],
    )
    output = ReviewSerializer(review)
    return Response(output.data, status=status.HTTP_201_CREATED)


@api_view(["PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def review_detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.reviewer_id != request.user.id:
        return Response(
            {"detail": "You do not have permission to modify this review."},
            status=status.HTTP_403_FORBIDDEN,
        )

    if request.method == "DELETE":
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = ReviewUpdateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    if "rating" in serializer.validated_data:
        review.rating = serializer.validated_data["rating"]
    if "description" in serializer.validated_data:
        review.description = serializer.validated_data["description"]
    review.save()

    output = ReviewSerializer(review)
    return Response(output.data, status=status.HTTP_200_OK)
