# blog/categories/api/permissions.py
# Rest framework modules
from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    If the user is admin can create, update, get and delete categories
    If the user is not admin can only read categories
    """
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_staff