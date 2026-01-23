from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from offerdetails_app.api.serializers import OfferDetailSerializer
from offerdetails_app.models import OfferDetail


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def offer_detail(request, detail_id):
    detail = get_object_or_404(OfferDetail, id=detail_id)
    serializer = OfferDetailSerializer(detail)
    return Response(serializer.data, status=status.HTTP_200_OK)
