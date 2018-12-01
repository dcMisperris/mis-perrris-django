from django.db import models


# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=30, null=False, default='Name-def')
    rut = models.CharField(max_length=9, null=False, default='1111-1')
    mail = models.EmailField(max_length=100, blank=False,default='mail@mail.cl')
    passwd = models.CharField(max_length=40, null=False, default='1234')
    img_persona = models.ImageField(default='default.jpg', blank=True)

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    OPCIONES_ESTADO = (('Rescatado', 'Rescatado'), ('Disponible', 'Disponible'), ('Adoptado', 'Adoptado'),)
    fotografia = models.ImageField(default='default.jpg', blank=True)
    nombre = models.CharField(max_length=30)
    raza_predominante = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.CharField(max_length=15, choices=OPCIONES_ESTADO, default='Rescatado')
    persona = models.ForeignKey(Persona, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
