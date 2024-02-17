from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


'''
    Crearemos dos modelos el primero para poder crear nuestro funcionario.
    Y el segundo para poder crear un token por cada usuario registrado
'''

class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    curp = curp = models.CharField(max_length=18, unique=True)
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    genero = models.JSONField()
    fecha_nacimiento = models.CharField(max_length=15)
    edad = models.IntegerField()
    estado = models.JSONField()
    
    def __str__(self):
        return self.curp
    
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if(created):
        Token.objects.create(user=instance)