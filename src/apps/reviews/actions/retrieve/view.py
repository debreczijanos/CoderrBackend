from rest_framework.response import Response
from rest_framework.views import APIView


class ReviewsRetrieveView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "retrieve", "resource": "reviews"})

    def post(self, request, *args, **kwargs):
        return Response({"action": "retrieve", "resource": "reviews"})

    def put(self, request, *args, **kwargs):
        return Response({"action": "retrieve", "resource": "reviews"})

    def delete(self, request, *args, **kwargs):
        return Response({"action": "retrieve", "resource": "reviews"})
