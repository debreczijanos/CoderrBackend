from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import (
    api_view,
    permission_classes,
    parser_classes,
    authentication_classes,
)
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.profiles.api.serializers import ProfileSerializer
from apps.profiles.models import Profile


@api_view(["GET", "PATCH"])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@authentication_classes([])
def profile_detail(request, user_id):
    profile = get_object_or_404(Profile, user_id=user_id)

    if request.method == "PATCH":
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Token "):
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        token_key = auth_header.split(" ", 1)[1].strip()
        token = Token.objects.filter(key=token_key).select_related("user").first()
        if not token:
            return Response(
                {"detail": "Invalid token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        if token.user.id != user_id:
            return Response(
                {"detail": "You do not have permission to edit this profile."},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    serializer = ProfileSerializer(profile)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def business_profiles(request):
    profiles = Profile.objects.filter(type=Profile.TYPE_BUSINESS).select_related("user")
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def customer_profiles(request):
    profiles = Profile.objects.filter(type=Profile.TYPE_CUSTOMER).select_related("user")
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
