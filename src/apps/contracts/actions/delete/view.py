from rest_framework.response import Response
from rest_framework.views import APIView


class ContractsDeleteView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "delete", "resource": "contracts"})

    def post(self, request, *args, **kwargs):
        return Response({"action": "delete", "resource": "contracts"})

    def put(self, request, *args, **kwargs):
        return Response({"action": "delete", "resource": "contracts"})

    def delete(self, request, *args, **kwargs):
        return Response({"action": "delete", "resource": "contracts"})
