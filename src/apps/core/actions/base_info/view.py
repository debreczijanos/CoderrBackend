from rest_framework.response import Response
from rest_framework.views import APIView


class BaseInfoView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"status": "ok", "offers": 0, "users": 0})
