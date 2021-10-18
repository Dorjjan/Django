from django.shortcuts import render
from api.models import Ubranie
from rest_framework import serializers, viewsets
from api.serializers import UbranieSerializers
class UbranieViewSets(viewsets.ModelViewSet):
     queryset = Ubranie.objects.all()  
     serializer_class = UbranieSerializers
