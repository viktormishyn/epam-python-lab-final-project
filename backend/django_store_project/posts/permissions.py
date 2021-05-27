from rest_framework.permissions import BasePermission, SAFE_METHODS


class PostUserWritePermission(BasePermission):
    # only author of the post can edit it
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            # SAFE_METHODS - GET, OPTIONS, HEAD
            return True
        return obj.author == request.user
