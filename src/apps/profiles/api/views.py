from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "PATCH"])
def profile_detail(request, user_id):
    return Response({"user": user_id})


@api_view(["GET"])
def business_profiles(request):
    return Response([])


@api_view(["GET"])
def customer_profiles(request):
    return Response([])
