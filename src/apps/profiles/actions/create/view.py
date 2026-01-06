from rest_framework.response import Response
from rest_framework.views import APIView


class ProfilesCreateView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "create", "resource": "profiles"})

    def post(self, request, *args, **kwargs):
        return Response({"action": "create", "resource": "profiles"})

    def put(self, request, *args, **kwargs):
        return Response({"action": "create", "resource": "profiles"})

    def delete(self, request, *args, **kwargs):
        return Response({"action": "create", "resource": "profiles"})
