from rest_framework import serializers
from Utiles.models import Paquete        

'''
    Crearemos el serializer para poder serializar y deserializar objetos del modelo Paquete 
    esto nos servira para poder crear un nuevo paquete o poder visualizarlo
    
'''

class PaqueteSerializers(serializers.ModelSerializer):
    
    '''
        El get_tutor_curp, get_beneficiario_curp uy get_institucion nos ayudara a recuperar el valor de los campos
        tutor_curp, beneficiario_curp y institucion 
    '''
    tutor_curp = serializers.SerializerMethodField()
    beneficiario_curp = serializers.SerializerMethodField()
    institucion = serializers.SerializerMethodField()
    
    class Meta:
        model = Paquete 
        #fields = '__all__'
        fields = ('id','numero_entrega','fecha_hora','tutor_curp','beneficiario_curp', 'institucion', 'direccion_entrega','entregado')
        
    def get_tutor_curp(self, obj):
        nombre = obj.solicitante.nombre + ' ' + obj.solicitante.primer_apellido + ' ' + obj.solicitante.segundo_apellido
        curp = obj.solicitante.curp
        soporte = nombre + ' ' + curp
        return soporte

    def get_beneficiario_curp(self, obj):
        nombre = obj.beneficiario.nombre + ' ' + obj.beneficiario.primer_apellido + ' ' + obj.beneficiario.segundo_apellido
        curp = obj.beneficiario.curp
        soporte = nombre + ' ' + curp
        return soporte
  
    def get_institucion(self, obj):
        return obj.institucion.nombre