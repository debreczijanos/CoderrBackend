from rest_framework.response import Response
from rest_framework.views import APIView


class ProfilesCustomerListView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"action": "profiles-customer-list", "resource": "profiles"})

