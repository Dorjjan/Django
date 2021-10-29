from django.shortcuts import render
from django.http import HttpResponse
from api.models import MensClothes, WomansClothes
from rest_framework import serializers, views, viewsets
from api.serializers import MensClothesSerializers, WomensClothesSerializers
class MensClothesViewSets(viewsets.ModelViewSet):
     queryset = MensClothes.objects.all()  
     serializer_class = MensClothesSerializers

class WomensClothesViewSets(viewsets.ModelViewSet):
     queryset = WomansClothes.objects.all()
     serializer_class = WomensClothesSerializers


def index(requset):
     query = MensClothes,WomansClothes.objects.all()
     return HttpResponse(query) 
def odziezMeska(requset):
     odziezMeska_user = MensClothes.objects.all()
     return HttpResponse(odziezMeska_user)
def odziezDamska(request):
     odziezDamska_user = WomansClothes.objects.all()
     return HttpResponse(odziezDamska_user)
