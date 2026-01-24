from rest_framework import serializers

from offerdetails_app.models import OfferDetail
from orders_app.models import Order


class OrderSerializer(serializers.ModelSerializer):
    """Serialize order data for API responses."""
    price = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)

    class Meta:
        model = Order
        fields = [
            "id",
            "customer_user",
            "business_user",
            "title",
            "revisions",
            "delivery_time_in_days",
            "price",
            "features",
            "offer_type",
            "status",
            "created_at",
            "updated_at",
        ]


class OrderCreateSerializer(serializers.Serializer):
    """Validate order creation payload."""
    offer_detail_id = serializers.IntegerField()

    def validate_offer_detail_id(self, value):
        """Ensure the offer detail exists."""
        if not OfferDetail.objects.filter(id=value).exists():
            raise serializers.ValidationError("Offer detail not found.")
        return value


class OrderStatusUpdateSerializer(serializers.Serializer):
    """Validate order status updates."""
    status = serializers.ChoiceField(choices=Order.STATUS_CHOICES)
