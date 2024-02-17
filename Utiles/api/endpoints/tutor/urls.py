from django.urls import path
from Utiles.api.endpoints.tutor.views import (TutorListAV, TutorDetalleAV, CreateTutor)

'''
    Creamos las urls de nuestro endpoint tutor
'''

urlpatterns = [
    # Las rutas que tienen que ver co los tutores
    path('all/', TutorListAV.as_view(), name='tutores-list'),
    path('tutor/<str:curp>/', TutorDetalleAV.as_view(), name='tutores-detalle'),
    path('create/', CreateTutor.as_view(), name='crear-tutor'),
]