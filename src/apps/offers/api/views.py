from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST"])
def offers_collection(request):
    return Response({"count": 0, "results": []})


@api_view(["GET", "PATCH", "DELETE"])
def offer_detail(request, offer_id):
    return Response({"id": offer_id})
