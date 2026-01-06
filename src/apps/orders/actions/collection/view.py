from rest_framework.response import Response
from rest_framework.views import APIView


class OrdersCollectionView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "orders-collection", "resource": "orders"})

    def post(self, request, *args, **kwargs):
        return Response({"action": "orders-collection", "resource": "orders"})

