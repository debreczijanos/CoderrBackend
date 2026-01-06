from rest_framework.response import Response
from rest_framework.views import APIView


class ReviewsCollectionView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "reviews-collection", "resource": "reviews"})

    def post(self, request, *args, **kwargs):
        return Response({"action": "reviews-collection", "resource": "reviews"})

