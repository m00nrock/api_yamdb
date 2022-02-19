from rest_framework import permissions

from django.conf import settings


class IsAuthorOrAdministrationOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        administration = settings.USER_AUTH and (settings.USER_ADMIN
                                                 or settings.USER_MOD)
        return (request.method in permissions.SAFE_METHODS
                or request.user == obj.author or administration)
