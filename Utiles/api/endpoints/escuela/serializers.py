from rest_framework import serializers
from Utiles.models import Escuela


'''
    Crearemos el serializer para poder serializar y deserializar objetos del modelo Escuela 
    esto nos servira para poder crear una nueva escuela.
    Esto nos ayudara ya que podremo consultar la escuela desde nuestro front
'''
class EscuelaSerializers(serializers.ModelSerializer):
    beneficiario_Escuela = serializers.StringRelatedField(many=True)
    class Meta:
        model = Escuela
        fields = '__all__' 