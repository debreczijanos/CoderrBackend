from rest_framework.response import Response
from rest_framework.views import APIView


class ProjectsCreateView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "create", "resource": "projects"})

    def post(self, request, *args, **kwargs):
        return Response({"action": "create", "resource": "projects"})

    def put(self, request, *args, **kwargs):
        return Response({"action": "create", "resource": "projects"})

    def delete(self, request, *args, **kwargs):
        return Response({"action": "create", "resource": "projects"})
