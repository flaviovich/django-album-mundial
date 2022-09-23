from email import message
from rest_framework.permissions import BasePermission
from rest_framework.request import Request

class PermisoPersonalizado(BasePermission):
    message = 'No hay permisos'
    def has_permission(self, request: Request, view):
        # sourcery skip: assign-if-exp, boolean-if-exp-identity, remove-unnecessary-cast
        if request.auth is None:
            return False

        if request.user.rol == 'ADMINISTRADOR':
            return False
        else:
            return True

class EsAdministrador(BasePermission):
    message = 'El usuario no tiene los permisos necesarios'
    def has_object_permission(self, request: Request, view):
        # sourcery skip: assign-if-exp, boolean-if-exp-identity, remove-unnecessary-cast
        if request.data.get('rol') == 'USUARIO':
            return True
        
        if request.auth is None:
            # self.message = 'Se necesita una token para esta peticion'
            return False

        if request.user.rol == 'ADMINISTRADOR':
            return True
        else:
            return False
            