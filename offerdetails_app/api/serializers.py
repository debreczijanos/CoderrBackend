from rest_framework import serializers

from offerdetails_app.models import OfferDetail


class OfferDetailSerializer(serializers.ModelSerializer):
    """Serialize offer detail fields."""
    price = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)

    class Meta:
        model = OfferDetail
        fields = [
            "id",
            "title",
            "revisions",
            "delivery_time_in_days",
            "price",
            "features",
            "offer_type",
        ]
