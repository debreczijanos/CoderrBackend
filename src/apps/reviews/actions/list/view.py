from rest_framework.response import Response
from rest_framework.views import APIView


class ReviewsListView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "list", "resource": "reviews"})

    def post(self, request, *args, **kwargs):
        return Response({"action": "list", "resource": "reviews"})

    def put(self, request, *args, **kwargs):
        return Response({"action": "list", "resource": "reviews"})

    def delete(self, request, *args, **kwargs):
        return Response({"action": "list", "resource": "reviews"})
