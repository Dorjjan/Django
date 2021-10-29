from rest_framework import serializers
from api.models import MensClothes, WomansClothes


class MensClothesSerializers(serializers.ModelSerializer):
    class Meta:
        model = MensClothes
        fields = ['nazwa', 'rozmiar', 'cena', 'kolor']

class WomensClothesSerializers(serializers.ModelSerializer):
    class Meta:
        model = WomansClothes
        fields= ['nazwa', 'rozmiar', 'cena', 'kolor']
