from rest_framework.response import Response
from rest_framework.views import APIView


class PaymentsCreateView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "create", "resource": "payments"})

    def post(self, request, *args, **kwargs):
        return Response({"action": "create", "resource": "payments"})

    def put(self, request, *args, **kwargs):
        return Response({"action": "create", "resource": "payments"})

    def delete(self, request, *args, **kwargs):
        return Response({"action": "create", "resource": "payments"})
