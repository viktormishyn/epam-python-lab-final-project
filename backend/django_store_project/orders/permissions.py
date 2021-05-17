from rest_framework.permissions import SAFE_METHODS, BasePermission


class isAdminOrReadOnly(BasePermission):
    message = 'Restricted to admin only'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or request.user.is_superuser:
            return True
        return False
