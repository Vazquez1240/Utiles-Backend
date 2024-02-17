from django.urls import path
from Utiles.api.endpoints.escuela.views import (EscuelasListAV, EscuelasDetalleAV,CreateEscuela)


'''
    Creamos las urls de nuestro endpoint escuelas
'''
urlpatterns = [
    # Las rutas que tienen que ver con escuelas
    path('all/', EscuelasListAV.as_view(), name='instituciones-lista'),
    path('institucion/<str:clave>', EscuelasDetalleAV.as_view(), name='institucion'),
    path('create/', CreateEscuela.as_view(), name='crear-institucion'),
]
