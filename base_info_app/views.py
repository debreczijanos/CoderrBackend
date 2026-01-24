from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthView(APIView):
    """Simple health check endpoint."""
    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request):
        """Return OK for uptime checks."""
        return Response({"status": "ok"})
