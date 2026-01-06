from rest_framework.response import Response
from rest_framework.views import APIView


class ProjectsListView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "list", "resource": "projects"})

    def post(self, request, *args, **kwargs):
        return Response({"action": "list", "resource": "projects"})

    def put(self, request, *args, **kwargs):
        return Response({"action": "list", "resource": "projects"})

    def delete(self, request, *args, **kwargs):
        return Response({"action": "list", "resource": "projects"})
