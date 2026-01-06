from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def login(request):
    return Response({"token": "", "user_id": None, "username": ""})


@api_view(["POST"])
def registration(request):
    return Response({"token": "", "user_id": None, "username": ""})
