from django.urls import path
from Utiles.api.endpoints.paquete.views import (PaqueteList, CreatePaquete,PaqueteDetalle,
                                               MarcarPaquete, PaqueteDetalleNumero)


'''
    Creamos las urls para nuestro endpoint Paquete:
    
    -all: nos servira para obtener todos los paquetes creados
    
    -detalle/<str:curp>/: nos servira para buscar un paquete por medio de una curp que tenga asociada
    
    -detalle-numero_entrega/<int:numero_entrega>/: nos servira para buscar un paquete por su numero de entrega
    
    -create: nos servir para crear un paquete
    
    <int:numero_entrega>/entregar/: nos ayudara para poder entregar un paquete por su numero de entrega
'''
urlpatterns = [
    # Las rutas que tienen que ver con escuelas
    path('all/',PaqueteList.as_view(), name='entregas-lista'),
    path('detalle/<str:curp>/', PaqueteDetalle.as_view(), name='paquete'),
    path('detalle-numero_entrega/<int:numero_entrega>/', PaqueteDetalleNumero.as_view(), name='paquete-numero_entrega'),
    path('create/', CreatePaquete.as_view(), name='crear-entrega'),
    path('<int:numero_entrega>/entregar/', MarcarPaquete.as_view(), name='crear-entrega'),
]