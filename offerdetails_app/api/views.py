from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from offerdetails_app.api.serializers import OfferDetailSerializer
from offerdetails_app.models import OfferDetail


class OfferDetailView(APIView):
    """Retrieve a single offer detail."""
    permission_classes = [IsAuthenticated]

    def get(self, request, detail_id):
        """Return offer detail fields for the given ID."""
        detail = get_object_or_404(OfferDetail, id=detail_id)
        serializer = OfferDetailSerializer(detail)
        return Response(serializer.data, status=status.HTTP_200_OK)
