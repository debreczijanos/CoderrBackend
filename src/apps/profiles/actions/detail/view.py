from rest_framework.response import Response
from rest_framework.views import APIView


class ProfilesDetailView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "profiles-detail", "resource": "profiles"})

    def patch(self, request, *args, **kwargs):
        return Response({"action": "profiles-detail", "resource": "profiles"})

