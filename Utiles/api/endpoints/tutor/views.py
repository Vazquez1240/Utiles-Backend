from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from Utiles.models import Tutor
from Utiles.api.endpoints.tutor.serializers import TutorSerializers


'''
    Aqui tenemos las views, explicare para que sirve cada una:
    
    -TutorListAV: Nos devuelve todos los tutores que existen
    
    -CreateTutor: Nos ayuda a crear un tutor
    
    -TutorDetalleAV: Nos ayudara a buscar un tutor por su curp
'''


class TutorListAV(APIView):
    
    #Funcion para obtener todos los tutores
    def get(self, request):
        tutores = Tutor.objects.all()
        serializer = TutorSerializers(tutores, many=True)
        # Devolvemos la data obtenida
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateTutor(APIView):
     def post(self, request):
        serializer = TutorSerializers(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TutorDetalleAV(APIView):
    
    def get(self, request, curp):
        try:
            tutor = Tutor.objects.get(curp=curp)
        except Tutor.DoesNotExist:
            return Response({'Error':"Persona no encotrada"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TutorSerializers(tutor)
        return Response(serializer.data)