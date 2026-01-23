from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from offerdetails_app.models import OfferDetail
from orders_app.api.serializers import (
    OrderCreateSerializer,
    OrderSerializer,
    OrderStatusUpdateSerializer,
)
from orders_app.models import Order
from profiles_app.models import Profile


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def orders_collection(request):
    if request.method == "GET":
        orders = Order.objects.filter(
            customer_user=request.user
        ) | Order.objects.filter(business_user=request.user)
        serializer = OrderSerializer(orders.order_by("-updated_at"), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    profile = Profile.objects.filter(user=request.user).first()
    if not profile or profile.type != Profile.TYPE_CUSTOMER:
        return Response(
            {"detail": "Only customers can create orders."},
            status=status.HTTP_403_FORBIDDEN,
        )

    serializer = OrderCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    detail = get_object_or_404(OfferDetail, id=serializer.validated_data["offer_detail_id"])
    order = Order.objects.create(
        customer_user=request.user,
        business_user=detail.offer.user,
        title=detail.title,
        revisions=detail.revisions,
        delivery_time_in_days=detail.delivery_time_in_days,
        price=detail.price,
        features=detail.features,
        offer_type=detail.offer_type,
    )
    output = OrderSerializer(order)
    return Response(output.data, status=status.HTTP_201_CREATED)


@api_view(["PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == "DELETE":
        if not request.user.is_staff:
            return Response(
                {"detail": "You do not have permission to delete this order."},
                status=status.HTTP_403_FORBIDDEN,
            )
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    profile = Profile.objects.filter(user=request.user).first()
    if not profile or profile.type != Profile.TYPE_BUSINESS:
        return Response(
            {"detail": "Only business users can update orders."},
            status=status.HTTP_403_FORBIDDEN,
        )
    if order.business_user_id != request.user.id:
        return Response(
            {"detail": "You do not have permission to update this order."},
            status=status.HTTP_403_FORBIDDEN,
        )

    serializer = OrderStatusUpdateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    order.status = serializer.validated_data["status"]
    order.save()
    output = OrderSerializer(order)
    return Response(output.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def order_count(request, profile_id):
    profile = Profile.objects.filter(user_id=profile_id).first()
    if not profile or profile.type != Profile.TYPE_BUSINESS:
        return Response(
            {"detail": "Business user not found."},
            status=status.HTTP_404_NOT_FOUND,
        )
    count = Order.objects.filter(
        business_user_id=profile_id, status=Order.STATUS_IN_PROGRESS
    ).count()
    return Response({"order_count": count}, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def order_completed_count(request, profile_id):
    profile = Profile.objects.filter(user_id=profile_id).first()
    if not profile or profile.type != Profile.TYPE_BUSINESS:
        return Response(
            {"detail": "Business user not found."},
            status=status.HTTP_404_NOT_FOUND,
        )
    count = Order.objects.filter(
        business_user_id=profile_id, status=Order.STATUS_COMPLETED
    ).count()
    return Response({"completed_order_count": count}, status=status.HTTP_200_OK)
