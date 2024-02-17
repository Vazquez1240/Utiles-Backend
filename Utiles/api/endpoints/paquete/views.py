
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from datetime import datetime
from Utiles.api.endpoints.paquete.permissions import IsAdminOrReadOnly
from Utiles.models import Paquete, Tutor, Beneficiario, Funcionario, Escuela
from Utiles.api.endpoints.paquete.serializers import PaqueteSerializers
from django.db.models import Q


'''
    Aqui tenemos las views, explicare para que sirve cada una:
    
    -PaqueteList: nos ayudara para obtener todos los paquetes creados
    
    -CreatePaquete: Nos ayudara para crear un nuevo paquete
    
    -MarcarPaquete: Nos ayudara para marcar un paquete como entregado cambiando su valor de false a true
    y agregando el funcionario que lo entrego con la hora de entrega 
    
    -PaqueteDetalle: nos ayudara para obtener los paquetes por medio de la curp que tengan asociada, puede ser del
    beneficiario o del solicitante, nos ayudamos de esta clase 'Q' que nos proporciona django que es para poder buscar
    objetos que cumplan con las condiciones en este caso se debe de esperar que devuelva mas de un objeto porque un beneficiario
    solo puede tener un paquete, pero un solicitate puede tener mas de un paquete asociado
    
    -PaqueteDetalleNumero: Nos servira para poder buscar un paquete por su numer de entrega
'''

class PaqueteList(APIView):
    permission_classes = [IsAdminOrReadOnly]
    # permission_classes = [IsAut]
    def get(self, request):
        paquetes = Paquete.objects.all()
        serializer = PaqueteSerializers(paquetes, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class CreatePaquete(APIView):
    def post(self, request, *args, **kwargs):
        
        serializer = PaqueteSerializers(data=request.data)
        if(serializer.is_valid()):
            tutor_curp = request.data.get('tutor_curp')
            beneficiario_curp = request.data.get('beneficiario_curp')
            institucion = request.data.get('institucion')
            
            try:
                tutor = Tutor.objects.get(curp=tutor_curp)
                beneficiario = Beneficiario.objects.get(curp=beneficiario_curp)
                institucion = Escuela.objects.get(clave=institucion)
            except Tutor.DoesNotExist:
                return Response({'Error':"Tutor no encotrada"}, status=status.HTTP_404_NOT_FOUND)
            
            except Beneficiario.DoesNotExist:
                 return Response({'Error':"Beneficiario no encotrada"}, status=status.HTTP_404_NOT_FOUND)
             
            except Escuela.DoesNotExist:
                 return Response({'Error':"Institucion no encotrada"}, status=status.HTTP_404_NOT_FOUND)
            
            if Paquete.objects.filter(beneficiario=beneficiario.id).exists():
                return Response({'Error': "El beneficiario ya tiene un paquete asignado"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save(beneficiario=beneficiario, solicitante_id = tutor.id, institucion_id = institucion.id)
                return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MarcarPaquete(APIView):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def put(self, request, numero_entrega):
        try:
            paquete = Paquete.objects.get(numero_entrega=numero_entrega)
            
        except Paquete.DoesNotExist:
            return Response({'Error':'No pudimos encontrar la entrega'}, status=status.HTTP_404_NOT_FOUND)
        
        user = request.user
        
        try:
            funcionario = get_object_or_404(Funcionario, user=user)
            
        except Funcionario.DoesNotExist:
            return Response({'Error':'No pudimos encontrar el funcionario'})
        
        if(paquete.entregado == True):
            return Response({'Error':'Ya se entrego ese paquete de utiles'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            paquete.entregado = True
            paquete.funcionario = funcionario
            paquete.fecha_entrega = datetime.now()
            paquete.save()
            return Response({'Mensaje': 'Paquete entregado correctamente'}, status=status.HTTP_200_OK)     


class PaqueteDetalle(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, curp):
        try:
            paquete = Paquete.objects.filter(Q(beneficiario__curp=curp) | Q(solicitante__curp=curp))
        except Paquete.DoesNotExist:
            return Response({'Error': 'Lo sentimos no pudimos encontrar esa entrega'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PaqueteSerializers(paquete, many=True)
        return Response(serializer.data)
    
    
class PaqueteDetalleNumero(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request, numero_entrega):
        try:
            paquete = Paquete.objects.get(numero_entrega=numero_entrega)
            
        except Paquete.DoesNotExist:
            return Response({'Error': 'Lo sentimos no pudimos encontrar esa entrega'})
        
        serializer = PaqueteSerializers(paquete)
        return Response(serializer.data)