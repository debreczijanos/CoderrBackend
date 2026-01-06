from rest_framework.response import Response
from rest_framework.views import APIView


class OrdersCountCompletedView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "orders-count-completed", "resource": "orders"})

