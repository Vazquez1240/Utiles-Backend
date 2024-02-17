from rest_framework import permissions

'''
    Esta clase nos permitira poner restrincciones a nuestras urls.
    Esta nos ayudara a que si el metodo es diferente a GET por decir un post o un put
    debe de tener en true el is_staff para poder realizar dicho metodo
'''
class IsAdminOrReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        if(request.method == 'GET'):
            return True
        else:
            admin_permission = bool(request.user.is_staff)
            return admin_permission