from rest_framework.response import Response
from rest_framework.views import APIView


class OrdersDetailView(APIView):
    def patch(self, request, *args, **kwargs):
        return Response({"action": "orders-detail", "resource": "orders"})

