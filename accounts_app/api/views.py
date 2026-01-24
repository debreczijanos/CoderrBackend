from django.contrib.auth import authenticate, get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts_app.api.serializers import LoginSerializer, RegistrationSerializer
from profiles_app.models import Profile


User = get_user_model()


class LoginView(APIView):
    """Authenticate a user and return an auth token."""
    permission_classes = [AllowAny]

    def post(self, request):
        """Validate credentials and issue a token."""
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request,
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )
        if not user:
            return Response(
                {"detail": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST
            )

        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "username": user.username,
                "email": user.email,
                "user_id": user.id,
            },
            status=status.HTTP_200_OK,
        )


class RegistrationView(APIView):
    """Register a new user and create a profile."""
    permission_classes = [AllowAny]

    def post(self, request):
        """Create user + profile and return an auth token."""
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.create_user(
            username=serializer.validated_data["username"],
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )
        Profile.objects.create(user=user, type=serializer.validated_data["type"])

        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "username": user.username,
                "email": user.email,
                "user_id": user.id,
            },
            status=status.HTTP_201_CREATED,
        )
