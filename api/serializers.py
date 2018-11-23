from rest_framework import serializers
from adopcion.models import Mascota

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ('id','nombre','fotografia','raza_predominante','descripcion','estado')