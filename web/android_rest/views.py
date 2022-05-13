import json

from django.shortcuts import render
from zerofire.models import Manager
from android_rest.serializers import ManagerSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser


# Create your views here.
def list(request):
    datalist = Manager.objects.get(mno=1)
    datalist2 = Manager.objects.get(name="김김김김")
    serializer = ManagerSerializer(datalist)
    serializer2 = ManagerSerializer(datalist2)
    Dout = [serializer,serializer2]
    for i in Dout:
        return JsonResponse(i.data,safe=False, json_dumps_params={'ensure_ascii':False})
