# blog/posts/api/permissions.py
# Rest framework modules
from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Permissions
    """
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else: 
            return request.user.is_staff