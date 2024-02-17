from django.db import models
import random
from funcionarios_app.models import Funcionario


'''
    Creamos esta funcion que nos ayudara a crear un numero random para cada entrega y ese sera el numeor de entrega
'''
def numero_random():
    while True:
        random_number = random.randint(1, 100000)  # Puedes ajustar los límites según tus necesidades
        if not Paquete.objects.filter(numero_entrega=random_number).exists():
            return random_number


class Escuela(models.Model):
    nombre = models.CharField(max_length=150)
    clave = models.CharField(max_length=150, unique=True)
    turno = models.CharField(max_length=25)
    colonia = models.CharField(max_length=150)
    calle = models.CharField(max_length=150)
    numero = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=200)
    region = models.CharField(max_length=50)
    zona_escolar =  models.CharField(max_length=50)
    clave_zona_escolar = models.IntegerField()
    nivel = models.CharField(max_length=50)
    subnivel = models.CharField(max_length=50)
    control = models.CharField(max_length=50)
    nombre_mostrar = models.CharField(max_length=500)
    geom = models.JSONField()
    
    
    def __str__(self):
        return self.nombre

class Tutor(models.Model):
    curp = models.CharField(max_length=18, unique=True)
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    genero = models.JSONField()
    fecha_nacimiento = models.CharField(max_length=15)
    edad = models.IntegerField()
    estado = models.JSONField()
    
    def __str__(self):
        return f'{self.nombre} {self.primer_apellido} {self.segundo_apellido} {self.curp}'
        #return  f'{self.nombre} {self.primer_apellido} {self.segundo_apellido}'
    
class Beneficiario(models.Model):
    curp = models.CharField(max_length=18, unique=True)
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    genero = models.JSONField()
    fecha_nacimiento = models.CharField(max_length=15)
    edad = models.IntegerField()
    estado = models.JSONField()
    numero_entrega = models.IntegerField(unique=True, blank=True, null=True)
    tutor = models.ForeignKey(Tutor, default=None, on_delete=models.CASCADE, related_name='beneficiario')
    escuela = models.ForeignKey(Escuela, default=None, on_delete=models.CASCADE, related_name='beneficiario_Escuela')
    
    def __str__(self):
        return   f'{self.nombre} {self.primer_apellido} {self.segundo_apellido} {self.curp}'
    
    
    
class Paquete(models.Model):
    solicitante = models.ForeignKey(Tutor,  on_delete=models.CASCADE, related_name='solicitante')
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE, related_name='beneficiario')
    numero_entrega = models.IntegerField(unique=True, default=numero_random)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='funcionario', blank=True, null=True)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    institucion = models.ForeignKey(Escuela, on_delete=models.CASCADE, related_name='institucion')
    entregado = models.BooleanField(default=False, null=False)
    fecha_entrega = models.DateTimeField(blank=True, null=True)
    direccion_entrega = models.CharField(max_length=150, null=False)
    
    def __str__(self):
        return f'{self.solicitante.curp} {self.numero_entrega}'
    
    def save(self, *args, **kwargs):
        if not self.beneficiario.numero_entrega:
            self.beneficiario.numero_entrega = self.numero_entrega
            self.beneficiario.save()
        super(Paquete, self).save(*args, **kwargs)