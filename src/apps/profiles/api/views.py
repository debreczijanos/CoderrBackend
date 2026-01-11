from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.profiles.api.serializers import ProfileDetailSerializer, ProfileListSerializer
from apps.profiles.models import Profile


@api_view(["GET", "PATCH"])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser, JSONParser])
def profile_detail(request, user_id):
    profile = get_object_or_404(Profile, user_id=user_id)

    if request.method == "PATCH":
        if request.user.id != user_id:
            return Response(
                {"detail": "You do not have permission to edit this profile."},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = ProfileDetailSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    serializer = ProfileDetailSerializer(profile)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def business_profiles(request):
    profiles = Profile.objects.filter(type=Profile.TYPE_BUSINESS).select_related("user")
    serializer = ProfileListSerializer(profiles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def customer_profiles(request):
    profiles = Profile.objects.filter(type=Profile.TYPE_CUSTOMER).select_related("user")
    serializer = ProfileListSerializer(profiles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
