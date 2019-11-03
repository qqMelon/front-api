from django.http import HttpResponse
from WarUnicorn.models import Unicorn, User
from WarUnicorn.serializers import UnicornSerializer, UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import viewsets
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class LoginView(APIView):
    """
    get logged
    """
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        if email is None or password is None:
            return Response(
                {"error": "Please provide both email and password"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = authenticate(email=email, password=password)
        if not user:
            return Response(
                {"error": "Invalid Credentials"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = TokenObtainPairSerializer(data=request.data)
        if serializer.is_valid():
            response = Response(data={"login": True}, status=status.HTTP_200_OK)
            response.set_cookie("JWT-access", serializer.validated_data["access"])
            response.set_cookie("JWT-refresh", serializer.validated_data["refresh"])
        return response


class UnicornList(APIView):
    """
    List all unicorns, or create a new one
    """

    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        unicorns = Unicorn.objects.all()
        serializer = UnicornSerializer(unicorns, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UnicornSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UnicornDetail(APIView):
    """
    Retrieve, update or delete an unicorn
    """

    def get_object(self, pk):
        try:
            return Unicorn.objects.get(pk=pk)
        except Unicorn.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        unicorn = self.get_object(pk)
        serializer = UnicornSerializer(unicorn)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        unicorn = self.get_object(pk)
        serializer = UnicornSerializer(unicorn, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        unicorn = self.get_object(pk)
        unicorn.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CanConnect(APIView):
    """
    Check is front can join back
    """

    def get(self, request, format=None):
        return HttpResponse(status=status.HTTP_200_OK)
