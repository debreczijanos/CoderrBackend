from rest_framework.response import Response
from rest_framework.views import APIView


class ProposalsRetrieveView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "retrieve", "resource": "proposals"})

    def post(self, request, *args, **kwargs):
        return Response({"action": "retrieve", "resource": "proposals"})

    def put(self, request, *args, **kwargs):
        return Response({"action": "retrieve", "resource": "proposals"})

    def delete(self, request, *args, **kwargs):
        return Response({"action": "retrieve", "resource": "proposals"})
