from rest_framework import viewsets
from .serializers import MascotaSerializer

class MascotaView(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
