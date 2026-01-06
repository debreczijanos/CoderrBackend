from rest_framework.response import Response
from rest_framework.views import APIView


class OfferdetailsDetailView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "offerdetails-detail", "resource": "offerdetails"})

