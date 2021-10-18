from rest_framework import serializers
from api.models import Ubranie
class UbranieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ubranie
        fields = ['nazwa', 'rozmiar', 'cena', 'plec']


