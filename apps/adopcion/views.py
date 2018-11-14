from django.shortcuts import render
from .models import Mascota

# Create your views here.
def index(request):
    return render(request,'index.html',{})

def adoptar(request):
    mascota= Mascota.objects.filter(estado = 'Disponible')

    contexto = {'mascotas':mascota}
    return render(request,'adoptar.html',contexto)

def registro(request):
    return render(request,'registrarse.html',{})

def sesion(request):
    return render(request,'iniciarsesion.html',{})

def lista_perros(request):
    mascota= Mascota.objects.filter(estado = 'Disponible')
    contexto = {'mascotas':mascota}
    return render(request,'lista_mascotas.html',contexto)

def mascotas_pitbull(request):
    mascota = Mascota.objects.filter(raza_predominante = 'Pitbull')
    contexto = {'mascotas':mascota}
    return render(request,'pitbulls.html',contexto)

def mascotas_pastores(request):
    mascota = Mascota.objects.filter(raza_predominante = 'pastor aleman')
    contexto = {'mascotas':mascota}
    return render(request,'pastores.html',contexto)
