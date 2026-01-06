from rest_framework.response import Response
from rest_framework.views import APIView


class ProfilesRetrieveView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "retrieve", "resource": "profiles"})

    def post(self, request, *args, **kwargs):
        return Response({"action": "retrieve", "resource": "profiles"})

    def put(self, request, *args, **kwargs):
        return Response({"action": "retrieve", "resource": "profiles"})

    def delete(self, request, *args, **kwargs):
        return Response({"action": "retrieve", "resource": "profiles"})
