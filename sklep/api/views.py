from django.shortcuts import render
from django.http import HttpResponse
from api.models import OdziezMeska, OdziezDamska
from rest_framework import serializers, views, viewsets
from api.serializers import OdziezMeskaSerializers, OdziezDamskaSerializers
class OdziezMeskaViewSets(viewsets.ModelViewSet):
     queryset = OdziezMeska.objects.all()  
     serializer_class = OdziezMeskaSerializers

class OdziezDamskaViewSets(viewsets.ModelViewSet):
     queryset = OdziezDamska.objects.all()
     serializer_class = OdziezDamskaSerializers


def index(requset):
     query = OdziezMeska,OdziezDamska.objects.all()
     return HttpResponse(query) 
def odziezMeska(requset):
     odziezMeska_user = OdziezMeska.objects.all()
     return HttpResponse(odziezMeska_user)
def odziezDamska(request):
     odziezDamska_user = OdziezDamska.object.all()
     return HttpResponse(odziezDamska_user)
