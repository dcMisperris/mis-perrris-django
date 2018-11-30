#from rest_framework import viewsets
from .serializers import MascotaSerializer
from .serializers import PersonaSerializer
from rest_framework import generics
#from rest_framework.permissions import IsAdminUser
from apps.adopcion.models import Mascota, Persona


class MascotaAPIView(generics.ListCreateAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class PersonaAPIView(generics.ListCreateAPIView):
    looup_field = 'pk'
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
