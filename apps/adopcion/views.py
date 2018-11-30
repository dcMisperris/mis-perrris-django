from django.shortcuts import render
from .models import Mascota, Persona
from django.http import JsonResponse



# Create your views here.
def test(request):
    persona = Persona.objects.all()
    context = {
        'mail' : 'some title here',
        'passwd' : 'password count'
    }
    return JsonResponse(context)


def home(request):
    return render(request,'adopcion/test.html',{})

def index(request):
    return render(request,'adopcion/index.html',{})

def adoptar(request):
    mascota= Mascota.objects.filter(estado = 'Disponible')

    contexto = {'mascotas':mascota}
    return render(request,'adopcion/adoptar.html',contexto)

def registro(request):
    return render(request,'adopcion/registrarse.html',{})

def sesion(request):
    return render(request,'adopcion/iniciarsesion.html',{})

def lista_mascotas(request):
    mascota= Mascota.objects.filter(estado = 'Disponible')
    contexto = {'mascotas':mascota}

    return render(request,'adopcion/lista_mascotas.html',contexto)

def mascotas_pitbull(request):
    mascota = Mascota.objects.filter(raza_predominante = 'Pitbull')
    contexto = {'mascotas':mascota}
    return render(request,'adopcion/pitbulls.html',contexto)

def mascotas_pastores(request):
    mascota = Mascota.objects.filter(raza_predominante = 'pastor aleman')
    contexto = {'mascotas':mascota}
    return render(request,'adopcion/pastores.html',contexto)

    ## rest_framework
