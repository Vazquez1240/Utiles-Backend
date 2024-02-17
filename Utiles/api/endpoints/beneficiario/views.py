from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from Utiles.models import Beneficiario, Tutor, Escuela
from Utiles.api.endpoints.beneficiario.serializers import BeneficiarioSerializers



'''
    Aqui tenemos las views, explicare para que sirve cada una:
    
    -BeneficiariosListAV: sirve para poder obtener todos los beneficiarios
    
    -CreateBeneficiario: nos servira para poder crear un nuevo beneficiario
    (se creo para poder crear mas beneficiarios para los ejemplos de la aplicacion)
    
    -BeneficiarioDetalleAV: sirve para poder buscar un beneficiario por su curp, esto en la aplicacion
    nos ayuda para poder comprobar que una curp de un beneficiario exista
'''

class BeneficiariosListAV(APIView):
    
    def get(self, request):
        beneficiarios = Beneficiario.objects.all()
        serializer = BeneficiarioSerializers(beneficiarios, many=True)
        # Devolvemos la data optenida 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class CreateBeneficiario(APIView):
    
    def post(self, request):
        serializer = BeneficiarioSerializers(data=request.data)
        if serializer.is_valid():
            # Aquí se asigna el tutor utilizando el tutor_id del JSON
            tutor_curp = request.data.get('tutor_curp')
            # Aqui se asigna la escuela utlizando el escuela_clave del JSON
            escuela_clave = request.data.get('escuela_clave')
            try:
                tutor = Tutor.objects.get(curp=tutor_curp)
                escuela = Escuela.objects.get(clave=escuela_clave)
                
            except Tutor.DoesNotExist:
                return Response({'Error':"Persona no encotrada"}, status=status.HTTP_404_NOT_FOUND)
            
            except Escuela.DoesNotExist:
                return Response({'Error':"Institucion no encotrada"}, status=status.HTTP_404_NOT_FOUND)
             
            beneficiario = serializer.save(tutor_id=tutor.id, escuela_id=escuela.id)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class BeneficiarioDetalleAV(APIView):
    
    def get(self, request, curp):
        try:
            beneficiario = Beneficiario.objects.get(curp=curp)
        except Beneficiario.DoesNotExist:
            return Response({'Error':"Persona no encotrada"}, status=status.HTTP_404_NOT_FOUND)
        
        serializers = BeneficiarioSerializers(beneficiario)
        return Response(serializers.data)