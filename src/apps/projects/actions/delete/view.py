from rest_framework.response import Response
from rest_framework.views import APIView


class ProjectsDeleteView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "delete", "resource": "projects"})

    def post(self, request, *args, **kwargs):
        return Response({"action": "delete", "resource": "projects"})

    def put(self, request, *args, **kwargs):
        return Response({"action": "delete", "resource": "projects"})

    def delete(self, request, *args, **kwargs):
        return Response({"action": "delete", "resource": "projects"})
