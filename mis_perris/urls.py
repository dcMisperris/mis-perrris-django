"""mis_perris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from api.views import PersonaAPIView,MascotaAPIView
from apps.adopcion.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',include('apps.adopcion.urls')),
    path('adoptar/',include('apps.adopcion.urls')),
    path('registro/',include('apps.adopcion.urls')),
    path('sesion/',include('apps.adopcion.urls')),
    path('pitbulls/',include('apps.adopcion.urls')),
    path('pastores/',include('apps.adopcion.urls')),
    #path('', include('apps.adopcion.urls')),
    url(r'^api/persona/',PersonaAPIView.as_view()),
    url(r'^api/mascota/',MascotaAPIView.as_view()),
    #path('test/',include('apps.adopcion.urls')),
    #url(r'^lista_persona/',persona_list),
    url(r'^home/',home),
    path('accounts/', include('allauth.urls'),)



]
