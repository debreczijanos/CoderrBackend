from rest_framework.response import Response
from rest_framework.views import APIView


class OrdersCountInProgressView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "orders-count-in-progress", "resource": "orders"})

