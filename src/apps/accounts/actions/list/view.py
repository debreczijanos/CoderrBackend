from rest_framework.response import Response
from rest_framework.views import APIView


class AccountsListView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "list", "resource": "accounts"})

    def post(self, request, *args, **kwargs):
        return Response({"action": "list", "resource": "accounts"})

    def put(self, request, *args, **kwargs):
        return Response({"action": "list", "resource": "accounts"})

    def delete(self, request, *args, **kwargs):
        return Response({"action": "list", "resource": "accounts"})
