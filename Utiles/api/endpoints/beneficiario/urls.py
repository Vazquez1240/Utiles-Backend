from django.urls import path
from Utiles.api.endpoints.beneficiario.views import (BeneficiariosListAV,BeneficiarioDetalleAV,CreateBeneficiario)


'''
    Estas serian las urls de nustro endpoint beneficiario
'''
urlpatterns = [
    # Las rutas que tienen que ver con los beneficiarios
    path('all/', BeneficiariosListAV.as_view(), name='lista-beneficiarios'),
    path('detalle/<str:curp>/', BeneficiarioDetalleAV.as_view(), name='detalle-beneficiario'),
    path('create/', CreateBeneficiario.as_view(), name='crear-beneficiario'),
]
