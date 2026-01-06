from rest_framework.response import Response
from rest_framework.views import APIView


class PaymentsUpdateView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "update", "resource": "payments"})

    def post(self, request, *args, **kwargs):
        return Response({"action": "update", "resource": "payments"})

    def put(self, request, *args, **kwargs):
        return Response({"action": "update", "resource": "payments"})

    def delete(self, request, *args, **kwargs):
        return Response({"action": "update", "resource": "payments"})
