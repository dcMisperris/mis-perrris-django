from .serializers import MascotaSerializer
from .serializers import PersonaSerializer
from rest_framework.permissions import IsAdminUser
from apps.adopcion.models import Mascota, Persona
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class MascotaAPIView(APIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer


class PersonaAPIView(APIView):
    def get(self, request):
    	personas = Persona.objects.all()
    	serialized = PersonaSerializer(personas, many= True)
    	return Response(serialized.data)

    def post(self,request,format=None):
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)