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

def list(request):
    if request.method == 'GET':
        datalist = Manager.objects.all()
        serializer = ManagerSerializer(datalist,many=True)
        return JsonResponse(serializer.data,safe=False, json_dumps_params={'ensure_ascii':False})

def loginandroid(request):
    if request.method == 'POST':
        data=JSONParser().parse(request)
        id= data["ID"]
        obj=Manager.objects.get(id=int(id))
        if data["PW"]==obj.pw_field:
            return JsonResponse("ok",safe=False, json_dumps_params={'ensure_ascii':False})
        else:
            return JsonResponse("fail",safe=False, json_dumps_params={'ensure_ascii':False})