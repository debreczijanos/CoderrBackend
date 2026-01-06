from rest_framework.response import Response
from rest_framework.views import APIView


class OffersDetailView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "offers-detail", "resource": "offers"})

    def patch(self, request, *args, **kwargs):
        return Response({"action": "offers-detail", "resource": "offers"})

    def delete(self, request, *args, **kwargs):
        return Response({"action": "offers-detail", "resource": "offers"})

