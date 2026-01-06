from rest_framework.response import Response
from rest_framework.views import APIView


class ContractsListView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "list", "resource": "contracts"})

    def post(self, request, *args, **kwargs):
        return Response({"action": "list", "resource": "contracts"})

    def put(self, request, *args, **kwargs):
        return Response({"action": "list", "resource": "contracts"})

    def delete(self, request, *args, **kwargs):
        return Response({"action": "list", "resource": "contracts"})
