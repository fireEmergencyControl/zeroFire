import json

from django.shortcuts import render
from zerofire.models import Manager
from android_rest.serializers import ManagerSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser


# Create your views here.
def list(request):
    datalist = Manager.objects.all()
    serializer = ManagerSerializer(datalist,many=True)
    return JsonResponse(serializer.data,safe=False, json_dumps_params={'ensure_ascii':False})