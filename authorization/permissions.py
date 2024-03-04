from rest_framework.permissions import BasePermission
from authorization.models import User

class IsSuperAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.SUPERADMIN
    
class IsCourier(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.COURIER
    
class IsBasic(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.BASIC