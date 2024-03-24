Sistema de Pre-Registros de Útiles Escolares
====

Este documento describe el backend de un sistema de pre-registros para útiles escolares. El sistema cuenta con los siguientes endpoints:

Todo lo que veremos sera para la parte de 'apiv1' despues veremos para el 'apiv2'

1.  'admin/': Esta ruta está reservada para la interfaz de administración de Django. Es donde puedes gestionar los modelos de datos registrados en tu aplicación mediante el panel de administración predeterminado de Django.

2. 'apiv1/responsable/': Esta ruta está diseñada para todo lo relacionado con el responsable (tutor encargado de registrar al menor en el registro). Este endpoint tiene la siguiente subdivisión.

   - 'apiv1/responsable/all/': Esta ruta te se encarga de devolver todos los responsables (tutores)
   - 'apiv1/responsable/ tutor/<str:curp>/': Esta ruta se encarga de buscar un tutor en especifico y como siguiente parametro se le pasa la curp para que asi lo pueda buscar
   - 'apiv1/responsable/ create/': Por utilmo esta ruta nos permitira crear un nuevo tutor esto para poder hacer mas pruebas y poder crearlos desde cero

3.  'apiv1/beneficiado/': Esta ruta esta diseñada para todo lo relacionado con el benediciado (El alummno que recibira los utiles). Este endpoint tiene la siguiente subdivisión.

     -  'apiv1/beneficiado/ all/ ': Esta ruta se encargar de traer todos los beneficiados registrados
     -  'apiv1/beneficiado/ detalle/<str:curp>/ ' : Esta ruta te mostrara los detalles de un beneficiado en especifico y para eso tenemos que pasarle la curp del beneficiado que queremos ver la informacion
     -  'apiv1/beneficiado/ create/': Por ultimo esta ruta nos permitira crar un nuevo beneficiado esto para poder hacer mas pruebas y poder crearlos desde cero

4.  'apiv1/institucion/': Esta ruta esta diseñada para todo lo relacionado con las instituciones (Escuelas). Este endpoint tiene la siguiente subdivisión.

     -  'apiv1/institucion/ all/': Esta ruta se encarga de buscar todas las instituciones y nos las muestra
     -  'apiv1/institucion/ institucion/<str:clave>': Esta ruta busca una unica institucion y lo hace mediante la clave de dicha institucion
     -  'apiv1/institucion/ create/': Esta ruta crea una nueva institucion esto para poder hacer mas pruebas y poder crearlos desde cero

5.  'apiv1/entrega/': Esta ruta esta diseñada para todo lo relacionado con las entregas (Son los paquetes de los utiles). Este endpoint tiene la siguiente subdivisión.

     -  'apiv1/entrega/ all/': Esta ruta se encarga de traer todas las entregas que se tiene hasta el momento.
     -  'apiv1/entrega/ detalle/<str:curp>/': Esta ruta se encarga de buscar una entrega mediante la curp del responsable (Tutor) o el beneficiado (Alumno)
     -  'apiv1/entrega/ detalle-numero_entrega/<int:numero_entrega>/': Esta ruta se encarga de buscar una entrega mediante el numero de la entrega (Este numero se obtiene al crear una nueva entrega)
     -  'apiv1/entrega/ create/': Esta ruta se encargara de crear las entregas, cada entrega es un paquete nuevo de utiles escolares.
     -  'apiv1/entrega/ <int:numero_entrega>/entregar/': Esta ruta se encargara de marcar como entregada la entrega y pide el numero de la entrega para poder buscarla y modificarla a entregada
  
Ahora si, la parte de 'apiv2' es para la parte de los funcionarios donde ellos se podran loguear y podran hacer varias cosas

1.  'apiv2/ login/': Esta ruta se encargara de hacer el login para los funcionarios y buscara en la app de funcionarios
2.  'apiv2/ register/': Esta ruta servira para registrar un nuevo funcionario.
3.  'apiv2/ logout/': Esta ruta se encargara de cerrar la sesion del funcionarion


Estas serian las rutas que componen el backen. Ahora les enseñare como instalar y correr el repositorio de manera local:

1.  Primero crearemos una nueva carpeta donde se guardara el repositorio
2.  Dentro de la carpeta ponemos el siguiente comando de git: "git clone https://github.com/Vazquez1240/Utiles-Backend.git" y presionamos ENTER
3.  Una ves que se descargo el repositorio vamos a ingresar a la carpeta del proyecto (Si esta desde la terminal puede hacer el siguiente comando "cd Utiles-Backend")
4.  Antes que nada se recomienda mucho utilizar Anaconda como manejador de entornos virtuales, para poder instalar todas las dependencias del repositorio y que no se instalen de manera global
5.  Vemos que el proyecto tiene la siguiente estructura:

   - ![image](https://github.com/Vazquez1240/Utiles-Backend/assets/127373642/4cee447d-d4da-422c-b63f-d47385a3e028)

6. Para poder instalar las dependencias nos ayudaremos del archivo requirements.txt, y utilizaremos el siguiente comando de pip: "pip install -r requirements.txt" y presionamos ENTER
7. Cuando se instalen todas las dependencias configuraremos la bd de datos, puede ser con sqlite como viene por definido pero se recomiendo utilizar Postgresql (Esta configuracion se hace en el archivo
  Settings.py que se encuentra en la carpeta principal del proyecto)

8. Despues haremos migraciones, primero utilizaremos el comando: "python manage.py makemigrations" y despues que se creen las migraciones las vamos a migrar a la base de datos con el siguiente comando "python manage.py migrate"
9. Ya con esto podemos crear un superusaurio con el siguiente comando: "python manage.py createsuperuser" esto nos pedira unos datos que utilizara para inicar sesion
10. Y por utimo podemos correr el proyecto con el comando "python manag.py runserver"

Y listo asi podemos correr el proyecto de manera local, Recuerda que los datos de la base de datos son los tuyos, tu usuario y contraseña, y el nombre de tu base de datos esto en caso de que utilices postgresql
si utilizas sqlite no hay problema ya que django la va a crear por ti solo tienes que agregarle lo siguiente:

```python
 DATABASES = {  
   'default': {  
     'ENGINE': 'django.db.backends.sqlite3',  
     'NAME': 'mydatabase',  
   }  
```
y de esta manera se va a crear un archivo db en tu proyecto. Te dejo una vista de como se ve el proyecto corriendo:
![image](https://github.com/Vazquez1240/Utiles-Backend/assets/127373642/5041011a-d482-4539-aec7-ebad7a0753cd)
