from rest_framework import permissions


class IsTutorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if request.user.is_tutor:
            return True
        return False


class IsStudentPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.add_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request, view):
        if request.user.is_student:
            return True
        return False


class IsSuperUserPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False