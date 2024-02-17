from rest_framework import serializers
from funcionarios_app.models import Funcionario
from django.contrib.auth.models import User
from rest_framework.response import Response

# creamos el serializer para poder serializar y deserializar objetos del modelo Funcionario esto nos servira para poder crear un nuevo funcionario 
class FuncionarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'

# Creamos un serializer para poder hacer un registro de un nuevo usuario
class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data['password']
        password2 = validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'Error': 'Las contraseñas no coinciden'})

        if User.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError({'Error': 'El email del usuario ya existe'})

        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(password)
        user.save()
        return user