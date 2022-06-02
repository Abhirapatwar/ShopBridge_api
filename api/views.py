from tkinter import E
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
import io
from api import serializers
from .models import Entries
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import Entries_serializer
from django.views.decorators.csrf import csrf_exempt

def homepage(request):
    return HttpResponse("<h1>Homepage</h1>")

@csrf_exempt
def Entriesapi(request):
    if request.method =='GET':
        e=Entries.objects.all()
        serialize=Entries_serializer(e, many=True)
        return JsonResponse(serialize.data, safe=False)

    if request.method =='POST':       
        pythondata=JSONParser().parse(request)
        Deserialize=Entries_serializer(data=pythondata)
        if Deserialize.is_valid():
            Deserialize.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)


@csrf_exempt
def Entries1api(request,pk):
    if request.method =='PUT':       
        pythondata=JSONParser().parse(request)
        # pk=pythondata.get('id', None)
        p=Entries.objects.get(id=pk)
        serialize=Entries_serializer(p, data=pythondata)
        if serialize.is_valid():
            serialize.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)   

    if request.method =='PATCH':
        pythondata=JSONParser().parse(request)
        p=Entries.objects.get(id=pk)
        serialize=Entries_serializer(p, data=pythondata, partial=True)
        if serialize.is_valid():
            serialize.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)         
        
    if request.method=='DELETE':
        # pythondata=JSONParser().parse(request)
        # pk=pythondata.get('id', None)
        e=Entries.objects.get(id=pk)
        e.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)       