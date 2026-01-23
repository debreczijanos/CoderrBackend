from django.urls import reverse
from rest_framework import serializers

from offerdetails_app.api.serializers import OfferDetailSerializer as OfferDetailItemSerializer
from offerdetails_app.models import OfferDetail
from offers_app.models import Offer


class OfferDetailInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    revisions = serializers.IntegerField()
    delivery_time_in_days = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)
    features = serializers.ListField(child=serializers.CharField(), allow_empty=True)
    offer_type = serializers.ChoiceField(choices=OfferDetail.TYPE_CHOICES)


class OfferCreateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField(allow_blank=True, required=False)
    image = serializers.FileField(required=False, allow_null=True)
    details = OfferDetailInputSerializer(many=True)

    def to_internal_value(self, data):
        if "details" not in data and "Details" in data:
            data = data.copy()
            data["details"] = data.get("Details")
        return super().to_internal_value(data)

    def validate_details(self, value):
        if len(value) != 3:
            raise serializers.ValidationError("Exactly 3 offer details are required.")
        types = {item["offer_type"] for item in value}
        if types != {
            OfferDetail.TYPE_BASIC,
            OfferDetail.TYPE_STANDARD,
            OfferDetail.TYPE_PREMIUM,
        }:
            raise serializers.ValidationError(
                "Offer details must include basic, standard, and premium."
            )
        return value


class OfferDetailUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    revisions = serializers.IntegerField(required=False)
    delivery_time_in_days = serializers.IntegerField(required=False)
    price = serializers.DecimalField(
        max_digits=10, decimal_places=2, coerce_to_string=False, required=False
    )
    features = serializers.ListField(child=serializers.CharField(), required=False)
    offer_type = serializers.ChoiceField(choices=OfferDetail.TYPE_CHOICES)


class OfferUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    description = serializers.CharField(allow_blank=True, required=False)
    image = serializers.FileField(required=False, allow_null=True)
    details = OfferDetailUpdateSerializer(many=True, required=False)

    def to_internal_value(self, data):
        if "details" not in data and "Details" in data:
            data = data.copy()
            data["details"] = data.get("Details")
        return super().to_internal_value(data)


class OfferDetailUrlSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    url = serializers.CharField()


class OfferListSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(source="user.id", read_only=True)
    details = serializers.SerializerMethodField()
    min_price = serializers.SerializerMethodField()
    min_delivery_time = serializers.SerializerMethodField()
    user_details = serializers.SerializerMethodField()

    class Meta:
        model = Offer
        fields = [
            "id",
            "user",
            "title",
            "image",
            "description",
            "created_at",
            "updated_at",
            "details",
            "min_price",
            "min_delivery_time",
            "user_details",
        ]

    def get_details(self, obj):
        details = []
        for detail in obj.details.all():
            details.append({"id": detail.id, "url": f"/offerdetails/{detail.id}/"})
        return details

    def get_min_price(self, obj):
        if hasattr(obj, "min_price") and obj.min_price is not None:
            return float(obj.min_price)
        prices = [detail.price for detail in obj.details.all()]
        return float(min(prices)) if prices else 0

    def get_min_delivery_time(self, obj):
        if hasattr(obj, "min_delivery_time") and obj.min_delivery_time is not None:
            return int(obj.min_delivery_time)
        times = [detail.delivery_time_in_days for detail in obj.details.all()]
        return min(times) if times else 0

    def get_user_details(self, obj):
        return {
            "first_name": obj.user.first_name or "",
            "last_name": obj.user.last_name or "",
            "username": obj.user.username,
        }


class OfferResponseSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(source="user.id", read_only=True)
    details = serializers.SerializerMethodField()
    min_price = serializers.SerializerMethodField()
    min_delivery_time = serializers.SerializerMethodField()

    class Meta:
        model = Offer
        fields = [
            "id",
            "user",
            "title",
            "image",
            "description",
            "created_at",
            "updated_at",
            "details",
            "min_price",
            "min_delivery_time",
        ]

    def get_details(self, obj):
        details = []
        for detail in obj.details.all():
            details.append({"id": detail.id, "url": f"/offerdetails/{detail.id}/"})
        return details

    def get_min_price(self, obj):
        prices = [detail.price for detail in obj.details.all()]
        return float(min(prices)) if prices else 0

    def get_min_delivery_time(self, obj):
        times = [detail.delivery_time_in_days for detail in obj.details.all()]
        return min(times) if times else 0


class OfferWithDetailsSerializer(serializers.ModelSerializer):
    details = OfferDetailItemSerializer(many=True)

    class Meta:
        model = Offer
        fields = [
            "id",
            "title",
            "image",
            "description",
            "details",
        ]
