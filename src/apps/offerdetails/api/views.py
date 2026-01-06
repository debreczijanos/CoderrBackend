from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def offer_detail(request, detail_id):
    return Response({"id": detail_id})
