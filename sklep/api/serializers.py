from rest_framework import serializers
from api.models import OdziezMeska, OdziezDamska, TypUbraniaM, TypUbraniaK


class OdziezMeskaSerializers(serializers.ModelSerializer):
    class Meta:
        model = OdziezMeska
        fields = ['nazwa', 'rozmiar', 'cena', 'kolor']

class OdziezDamskaSerializers(serializers.ModelSerializer):
    class Meta:
        model = OdziezDamska
        fields= ['nazwa', 'rozmiar', 'cena', 'kolor']
class TypUbraniaMSerializers(serializers.ModelSerializer):
    class Meta:
        model = TypUbraniaM
        fields = ["typ"]
class TypUbraniaKSerializers(serializers.ModelSerializer):
    class Meta:
        model = TypUbraniaK
        fields = ["typ"]