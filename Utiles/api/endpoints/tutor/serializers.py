from Utiles.models import Tutor
from rest_framework import serializers

'''
    Crearemos el serializer para poder serializar y deserializar objetos del modelo Tutor 
    esto nos servira para poder crear un nuevo tutor o poder visualizarlo
    
'''

class TutorSerializers(serializers.ModelSerializer):
    beneficiario = serializers.StringRelatedField(many=True)
    class Meta:
        model = Tutor
        fields = '__all__'