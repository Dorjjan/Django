from rest_framework import serializers
from api.models import OdziezMeska, OdziezDamska


class OdziezMeskaSerializers(serializers.ModelSerializer):
    class Meta:
        model = OdziezMeska
        fields = ['nazwa', 'rozmiar', 'cena', 'kolor']

class OdziezDamskaSerializers(serializers.ModelSerializer):
    class Meta:
        model = OdziezDamska
        fields= ['nazwa', 'rozmiar', 'cena', 'kolor']
