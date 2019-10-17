from django.contrib.auth.models import User, Group
from rest_framework import viewsets

# from WarUnicorn.serializers import UserSerializer, GroupSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from WarUnicorn.models import Unicorn
from WarUnicorn.serializers import UnicornSerializer


@csrf_exempt
def unicorn_list(request):
    """
    List all unicorns, or create a new one
    """
    if request.method == 'GET':
        unicorns = Unicorn.objects.all()
        serializer = UnicornSerializer(unicorns, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UnicornSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def unicorn_detail(request, pk):
    """
    Retrieve, update or delete an unicorn
    """
    try:
        unicorn = Unicorn.objects.get(pk=pk)
    except Unicorn.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UnicornSerializer(unicorn)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UnicornSerializer(unicorn, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        unicorn.delete()
        return HttpResponse(status=204)


@csrf_exempt
def can_connect(request):
    """
    Check is front can join back
    """
    return HttpResponse(status=200)
