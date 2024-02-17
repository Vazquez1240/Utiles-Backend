from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from funcionarios_app.api.views import Registration_view, logout_view

# configuramos las urls de nuestra app funcionarios_app
urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', Registration_view, name='registrer'),
    path('logout/', logout_view, name='logout'),
]
