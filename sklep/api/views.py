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
def odziezMeska(requset):
     odziezMeska_user = OdziezMeska.objects.all()
     return HttpResponse(odziezMeska_user)
def odziezDamska(request):
     odziezDamska_user = OdziezDamska.objects.all()
     return HttpResponse(odziezDamska_user)
def odziezMeskaTyp(request, id):
     odziezMeskaTyp_user = TypUbraniaM.objects.get(pk=id)
     return(odziezMeskaTyp_user.typ)