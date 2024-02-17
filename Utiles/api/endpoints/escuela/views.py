
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from Utiles.models import Escuela
from Utiles.api.endpoints.escuela.serializers import EscuelaSerializers


'''
    Aqui tenemos las views, explicare para que sirve cada una:
    
    -EscuelasListAV : Nos devolvera todas las escuelas que estan registradas
    
    -CreateEscuela : se usara para crear escuelas (esto para tener la manera de crearlas de esta manera sin el django administration)
    
    -EscuelasDetalleAV : buscara una escuela por su clave
'''

class EscuelasListAV(APIView):
    
    def get(self,request):
        escuelas = Escuela.objects.all()
        serializer = EscuelaSerializers(escuelas, many=True)
        # Devolvemos la data optenida
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class CreateEscuela(APIView):
    def post(self, request):
        serializer = EscuelaSerializers(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EscuelasDetalleAV(APIView):
    
    def get(self, request, clave):
        try:
            escuela = Escuela.objects.get(clave=clave)
        except Escuela.DoesNotExist:
            return Response({'Error':'Lo sentimos no hemos podido encotrar esa institucion'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = EscuelaSerializers(escuela)
        return Response(serializer.data)    