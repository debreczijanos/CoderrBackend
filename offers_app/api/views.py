from django.db.models import Min, Q
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from offerdetails_app.models import OfferDetail
from offers_app.api.serializers import (
    OfferCreateSerializer,
    OfferListSerializer,
    OfferResponseSerializer,
    OfferUpdateSerializer,
    OfferWithDetailsSerializer,
)
from offers_app.models import Offer
from profiles_app.models import Profile


class OffersCollectionView(APIView):
    """List offers or create a new offer."""
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get(self, request):
        """Return a paginated list of offers with optional filters."""
        queryset = (
            Offer.objects.select_related("user")
            .prefetch_related("details")
            .annotate(
                min_price=Min("details__price"),
                min_delivery_time=Min("details__delivery_time_in_days"),
            )
        )

        creator_id = request.query_params.get("creator_id")
        if creator_id:
            if not creator_id.isdigit():
                return Response(
                    {"detail": "creator_id must be an integer."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            queryset = queryset.filter(user_id=int(creator_id))

        min_price = request.query_params.get("min_price")
        if min_price:
            try:
                min_price_value = float(min_price)
            except ValueError:
                return Response(
                    {"detail": "min_price must be a number."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            queryset = queryset.filter(min_price__gte=min_price_value)

        max_delivery_time = request.query_params.get("max_delivery_time")
        if max_delivery_time:
            if not max_delivery_time.isdigit():
                return Response(
                    {"detail": "max_delivery_time must be an integer."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            queryset = queryset.filter(min_delivery_time__lte=int(max_delivery_time))

        search = request.query_params.get("search")
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(description__icontains=search)
            )

        ordering = request.query_params.get("ordering")
        if ordering in {"updated_at", "-updated_at", "min_price", "-min_price"}:
            queryset = queryset.order_by(ordering)

        paginator = PageNumberPagination()
        page_size = request.query_params.get("page_size")
        if page_size and page_size.isdigit():
            paginator.page_size = int(page_size)
        page = paginator.paginate_queryset(queryset, request)
        serializer = OfferListSerializer(page, many=True, context={"request": request})
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        """Create a new offer for a business user."""
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        profile = Profile.objects.filter(user=request.user).first()
        if not profile or profile.type != Profile.TYPE_BUSINESS:
            return Response(
                {"detail": "Only business users can create offers."},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = OfferCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        offer = Offer.objects.create(
            user=request.user,
            title=serializer.validated_data["title"],
            description=serializer.validated_data.get("description", ""),
            image=serializer.validated_data.get("image"),
        )
        for detail in serializer.validated_data["details"]:
            OfferDetail.objects.create(offer=offer, **detail)

        output = OfferWithDetailsSerializer(offer, context={"request": request})
        return Response(output.data, status=status.HTTP_201_CREATED)


class OfferDetailView(APIView):
    """Retrieve, update, or delete a single offer."""
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get(self, request, offer_id):
        """Return full offer details for the given ID."""
        offer = get_object_or_404(
            Offer.objects.select_related("user").prefetch_related("details"), id=offer_id
        )
        serializer = OfferResponseSerializer(offer, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, offer_id):
        """Update offer fields and detail items owned by the requester."""
        offer = get_object_or_404(
            Offer.objects.select_related("user").prefetch_related("details"), id=offer_id
        )
        if offer.user_id != request.user.id:
            return Response(
                {"detail": "You do not have permission to modify this offer."},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = OfferUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if "title" in serializer.validated_data:
            offer.title = serializer.validated_data["title"]
        if "description" in serializer.validated_data:
            offer.description = serializer.validated_data["description"]
        if "image" in serializer.validated_data:
            offer.image = serializer.validated_data["image"]
        offer.save()

        details_payload = serializer.validated_data.get("details")
        if details_payload is not None:
            for detail_data in details_payload:
                offer_type = detail_data.get("offer_type")
                if not offer_type:
                    return Response(
                        {"detail": "offer_type is required for detail updates."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                detail = offer.details.filter(offer_type=offer_type).first()
                if not detail:
                    return Response(
                        {"detail": f"Detail not found for offer_type '{offer_type}'."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                for field in [
                    "title",
                    "revisions",
                    "delivery_time_in_days",
                    "price",
                    "features",
                ]:
                    if field in detail_data:
                        setattr(detail, field, detail_data[field])
                detail.save()

        # Clear prefetched details to avoid stale data in the response.
        if hasattr(offer, "_prefetched_objects_cache"):
            offer._prefetched_objects_cache.pop("details", None)

        output = OfferWithDetailsSerializer(offer, context={"request": request})
        return Response(output.data, status=status.HTTP_200_OK)

    def delete(self, request, offer_id):
        """Delete the offer if the requester is the owner."""
        offer = get_object_or_404(
            Offer.objects.select_related("user").prefetch_related("details"), id=offer_id
        )
        if offer.user_id != request.user.id:
            return Response(
                {"detail": "You do not have permission to modify this offer."},
                status=status.HTTP_403_FORBIDDEN,
            )
        offer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
