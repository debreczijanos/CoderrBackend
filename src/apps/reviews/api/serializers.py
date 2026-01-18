from rest_framework import serializers

from apps.reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
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
    business_user = serializers.IntegerField()
    rating = serializers.IntegerField(min_value=1, max_value=5)
    description = serializers.CharField(allow_blank=True)


class ReviewUpdateSerializer(serializers.Serializer):
    rating = serializers.IntegerField(min_value=1, max_value=5, required=False)
    description = serializers.CharField(allow_blank=True, required=False)
