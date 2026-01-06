from rest_framework.response import Response
from rest_framework.views import APIView


class AccountsCreateView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "create", "resource": "accounts"})

    def post(self, request, *args, **kwargs):
        return Response({"action": "create", "resource": "accounts"})

    def put(self, request, *args, **kwargs):
        return Response({"action": "create", "resource": "accounts"})

    def delete(self, request, *args, **kwargs):
        return Response({"action": "create", "resource": "accounts"})
