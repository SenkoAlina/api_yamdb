from rest_framework import permissions


class AdminPermission(permissions.BasePermission):
    def has_object_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == 'admin')
