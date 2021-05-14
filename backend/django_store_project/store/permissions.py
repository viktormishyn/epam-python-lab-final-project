from rest_framework.permissions import BasePermission, SAFE_METHODS


class isAdminOrReadOnly(BasePermission):
    message = 'Restricted to admin only'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or request.user.is_superuser:
            return True
        return False


class StaffPostGamePermission(BasePermission):
    # only staff is allowed to post games, but only superuser is allowed to delete all games
    message = 'Adding new games is restricted to staff only'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or request.user.is_superuser:
            # GET, OPTIONS, HEAD
            return True
        return request.user.is_staff and request.method != 'DELETE'


class StaffPutDeleteGamePermission(BasePermission):
    # only staff is allowed to update and delete games
    message = 'Updating and deleting games is restricted to staff only'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff
