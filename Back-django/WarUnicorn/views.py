from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from WarUnicorn.models import Unicorn
from WarUnicorn.serializers import UnicornSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView


class UnicornList(APIView):
    """
    List all unicorns, or create a new one
    """

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
