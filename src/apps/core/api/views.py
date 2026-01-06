from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def base_info(request):
    return Response({"status": "ok", "offers": 0, "users": 0})
