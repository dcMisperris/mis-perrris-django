from rest_framework import serializers
from apps.adopcion.models import Mascota , Persona

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ('id','nombre','fotografia','raza_predominante','descripcion','estado')

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('pk','nombre','mail', 'passwd','img_persona','rut')
