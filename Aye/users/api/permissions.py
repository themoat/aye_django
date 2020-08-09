from rest_framework import permissions

class IsOwnerorReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_methods:
            return True
        return obj.owner == request.user


