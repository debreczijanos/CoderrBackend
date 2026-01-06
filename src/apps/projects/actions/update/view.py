from rest_framework.response import Response
from rest_framework.views import APIView


class ProjectsUpdateView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "update", "resource": "projects"})

    def post(self, request, *args, **kwargs):
        return Response({"action": "update", "resource": "projects"})

    def put(self, request, *args, **kwargs):
        return Response({"action": "update", "resource": "projects"})

    def delete(self, request, *args, **kwargs):
        return Response({"action": "update", "resource": "projects"})
