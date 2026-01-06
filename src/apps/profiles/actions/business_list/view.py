from rest_framework.response import Response
from rest_framework.views import APIView


class ProfilesBusinessListView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "profiles-business-list", "resource": "profiles"})

