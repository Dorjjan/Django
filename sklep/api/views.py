from django.shortcuts import render
from django.http import HttpResponse
from api.models import OdziezMeska, OdziezDamska,TypUbraniaM, TypUbraniaK
from rest_framework import serializers, views, viewsets
from api.serializers import OdziezMeskaSerializers, OdziezDamskaSerializers,TypUbraniaMSerializers,TypUbraniaKSerializers
class OdziezMeskaViewSets(viewsets.ModelViewSet):
     queryset = OdziezMeska.objects.all()  
     serializer_class = OdziezMeskaSerializers

class OdziezDamskaViewSets(viewsets.ModelViewSet):
     queryset = OdziezDamska.objects.all()
     serializer_class = OdziezDamskaSerializers
class TypUbraniaMViewSets(viewsets.ModelViewSet):
     queryset = TypUbraniaM.objects.all()
     serializer_class = TypUbraniaMSerializers

class TypUbraniaKViewSets(viewsets.ModelViewSet):
     queryset = TypUbraniaK.objects.all()
     serializer_class = TypUbraniaKSerializers
def index(requset):
     query = OdziezMeska,OdziezDamska.objects.all()
     return HttpResponse(query) 
