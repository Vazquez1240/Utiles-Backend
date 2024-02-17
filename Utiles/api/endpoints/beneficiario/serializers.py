from rest_framework import serializers
from Utiles.models import Beneficiario

'''
    Crearemos el serializer para poder serializar y deserializar objetos del modelo Beneficiario 
    esto nos servira para poder crear un nuevo Beneficiario 
    
'''
class BeneficiarioSerializers(serializers.ModelSerializer):
    
    '''
        El get_tutor_curp y el get_escuela_clave nos ayudara a recuperar el valor de los campos tutor_curp y escuela_clave
    '''
    tutor_curp = serializers.SerializerMethodField() 
    escuela_clave = serializers.SerializerMethodField()
    
    class Meta:
        model = Beneficiario
        fields = ('id', 'curp', 'nombre', 'primer_apellido', 'segundo_apellido', 'sexo', 'genero', 'fecha_nacimiento', 'edad', 'estado', 'tutor_curp', 'escuela_clave')
        read_only_fields = ('tutor_id',)
        
    def get_tutor_curp(self, obj):
        return obj.tutor.curp

    def get_escuela_clave(self, obj):
        return obj.escuela.clave