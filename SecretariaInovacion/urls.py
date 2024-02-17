from django.contrib import admin
from django.urls import path, include

'''
    En esta parte se van a crear las urls para las diferentes aplicaciones que tenemos en nuestro proyecto
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Estas son las urls de la primer api que es la de utiles
    path('apiv1/responsable/', include('Utiles.api.endpoints.tutor.urls')),
    path('apiv1/beneficiado/', include('Utiles.api.endpoints.beneficiario.urls')),
    path('apiv1/institucion/', include('Utiles.api.endpoints.escuela.urls')),
    path('apiv1/entrega/', include('Utiles.api.endpoints.paquete.urls')),
    
    # Aqui estara la url de la apiv2 que es la de funcionarios_app
    path('apiv2/', include('funcionarios_app.api.urls')),
    
    #path('api-auth/', include('rest_framework.urls'))
]