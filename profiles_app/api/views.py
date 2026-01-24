from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles_app.api.serializers import ProfileDetailSerializer, ProfileListSerializer
from profiles_app.models import Profile


class ProfileDetailView(APIView):
    """Retrieve or update a single user profile."""
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get(self, request, user_id):
        """Return the profile data for the given user ID."""
        profile = get_object_or_404(Profile, user_id=user_id)
        serializer = ProfileDetailSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, user_id):
        """Update the profile if the requester owns it."""
        profile = get_object_or_404(Profile, user_id=user_id)
        if request.user.id != user_id:
            return Response(
                {"detail": "You do not have permission to edit this profile."},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = ProfileDetailSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class BusinessProfilesView(APIView):
    """List all business profiles."""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Return a list of business profiles."""
        profiles = Profile.objects.filter(type=Profile.TYPE_BUSINESS).select_related(
            "user"
        )
        serializer = ProfileListSerializer(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomerProfilesView(APIView):
    """List all customer profiles."""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Return a list of customer profiles."""
        profiles = Profile.objects.filter(type=Profile.TYPE_CUSTOMER).select_related(
            "user"
        )
        serializer = ProfileListSerializer(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
