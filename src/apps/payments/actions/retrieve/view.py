from rest_framework.response import Response
from rest_framework.views import APIView


class PaymentsRetrieveView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "retrieve", "resource": "payments"})

    def post(self, request, *args, **kwargs):
        return Response({"action": "retrieve", "resource": "payments"})

    def put(self, request, *args, **kwargs):
        return Response({"action": "retrieve", "resource": "payments"})

    def delete(self, request, *args, **kwargs):
        return Response({"action": "retrieve", "resource": "payments"})
