from rest_framework import permissions


class IsAuthenticatedAndSelfOrMakeReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow creators of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
            return True
        if not request.user.is_authenticated:
            return False
        return obj.designer == request.user


class IsAuthenticatedAndSelf(permissions.BasePermission):
    """
    Custom permission to only allow creators of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        return obj.designer == request.user
