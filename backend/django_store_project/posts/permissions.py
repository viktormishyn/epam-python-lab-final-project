from rest_framework.permissions import BasePermission


class PutDeleteCommentsPermission(BasePermission):
    message = 'Editing or deleting posts is restricted to the author, manager or admin'

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.author == request.user
