from django.contrib import admin
from Utiles.models import Tutor, Escuela, Beneficiario, Paquete
from funcionarios_app.models import Funcionario

'''
    Registramos nuestros modelos
'''

admin.site.register(Tutor)
admin.site.register(Escuela)
admin.site.register(Beneficiario)
admin.site.register(Funcionario)
admin.site.register(Paquete)