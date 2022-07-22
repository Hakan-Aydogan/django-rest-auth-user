from rest_framework import permissions


class KendiProfilYadaReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if request.method == permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class DurumMesajıSabibiYadaReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if request.method == permissions.SAFE_METHODS:
            return True
        return obj.profil == request.user.profil
