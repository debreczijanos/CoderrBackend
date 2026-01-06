from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST"])
def reviews_collection(request):
    return Response([])


@api_view(["PATCH", "DELETE"])
def review_detail(request, review_id):
    return Response({"id": review_id})
