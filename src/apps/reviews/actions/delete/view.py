from rest_framework.response import Response
from rest_framework.views import APIView


class ReviewsDeleteView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "delete", "resource": "reviews"})

    def post(self, request, *args, **kwargs):
        return Response({"action": "delete", "resource": "reviews"})

    def put(self, request, *args, **kwargs):
        return Response({"action": "delete", "resource": "reviews"})

    def delete(self, request, *args, **kwargs):
        return Response({"action": "delete", "resource": "reviews"})
