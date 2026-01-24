from rest_framework import serializers

from reviews_app.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """Serialize review data for responses."""
    class Meta:
        model = Review
        fields = [
            "id",
            "business_user",
            "reviewer",
            "rating",
            "description",
            "created_at",
            "updated_at",
        ]


class ReviewCreateSerializer(serializers.Serializer):
    """Validate review creation payload."""
    business_user = serializers.IntegerField()
    rating = serializers.IntegerField(min_value=1, max_value=5)
    description = serializers.CharField(allow_blank=True)


class ReviewUpdateSerializer(serializers.Serializer):
    """Validate review updates."""
    rating = serializers.IntegerField(min_value=1, max_value=5, required=False)
    description = serializers.CharField(allow_blank=True, required=False)
