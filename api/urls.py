from django.conf.urls import url
from .views import *
from django.urls import path,include

urlpatterns = {

    path(r'^persona/',PersonaAPIView.as_view(), name ='persona-api'),
    path(r'^mascota/',MascotaAPIView.as_view(), name='mascota-api'),

}
