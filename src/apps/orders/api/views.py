from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST"])
def orders_collection(request):
    return Response([])


@api_view(["PATCH"])
def order_detail(request, order_id):
    return Response({"id": order_id})


@api_view(["GET"])
def order_count(request, profile_id):
    return Response({"order_count": 0})


@api_view(["GET"])
def order_completed_count(request, profile_id):
    return Response({"order_count": 0})
