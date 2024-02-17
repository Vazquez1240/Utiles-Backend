from rest_framework.decorators import api_view
from rest_framework.response import Response
from funcionarios_app.api.serializers import RegistrationSerializer, FuncionarioSerializers
from rest_framework import status
from funcionarios_app import models
from rest_framework.authtoken.models import Token



# crearemos la view de logout view que nos servira para el cierre se sesion
@api_view(['POST'])
def logout_view(request):
    if(request.method == 'POST'): # verifica si la solicitud es de tipo post
        request.user.auth_token.delete() # si es de tipo post toma el token del usuario al que pertenece el token y lo elimina (se genera uno cada inicio de sesion)
        return Response(status=status.HTTP_200_OK)


# esta es la view para poder registrar un nuevo funcionario
@api_view(['POST'])
def Registration_view(request):
    if request.method == 'POST': # verifica que el metodo sea post y si es hara lo siguiente
        user_serializer = RegistrationSerializer(data=request.data) # llamaremos al serializer que creamos para poder registrar un nuevo usuario

        if user_serializer.is_valid(): # si user_serializer es valido seguira con el proceso (la comprobacion de las contraseñas y que el email no exista se realiza en el serializer)
            user = user_serializer.save() # se guarda el usuario
        
            
            token = Token.objects.get(user=user).key # obtenemos el token que se le asigno al usuario que se acaba de crear
            
            data = {} # creamos un diccionario vacio llamado data
            
            '''
                Creamos un diccionario vacio llamao funcionario data que nos servira para poder enviar la data para poder 
                crear el funcionario 
            '''
            funcionario_data = {
                'user': user.id, 
                'curp': request.data.get('curp'),
                'nombre': request.data.get('nombre'),
                'primer_apellido': request.data.get('primer_apellido'),
                'segundo_apellido' : request.data.get('segundo_apellido'),
                'sexo' : request.data.get('sexo'),
                'genero' : request.data.get('genero'),
                'fecha_nacimiento':request.data.get('fecha_nacimiento'),
                'edad':request.data.get('edad'),
                'estado':request.data.get('estado'),
            }
            
            '''
                Llamamos al serializer que creamos para poder crear un nuevo funcionario y le
                pasamos la data (que es el diccionario que creamos anteriormete)
            '''
            
            funcionario_serializer = FuncionarioSerializers(data=funcionario_data) 

            if funcionario_serializer.is_valid(): # verificamos que todo este bien y que sea validos los datos
                funcionario_serializer.save() # si todo sale bien se guarda el funcionario
                
                '''
                    Al diccionario que llamamos data le agregaremos dos claves nuevas.
                    Una llamada username que tendra el usuario que se acaba de crear.
                    Y otra llamada token donde el valor sera el valor del token que se creo
                    (Esto nos servira para retornar os valores al usuario)
                '''
                data['username']  = user.username
                data['token'] = token
                
                return Response(data, status=status.HTTP_201_CREATED) 
            else:
                user.delete()  # Si la creación del Funcionario falla, elimina el usuario
                return Response(funcionario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    