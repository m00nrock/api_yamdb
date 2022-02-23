from rest_framework import permissions

from django.conf import settings


class IsAuthorOrAdministrationOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        USER_AUTH = request.user.is_authenicated
        USER_ADMIN = request.user.is_admin
        USER_MOD = request.user.is_moderator
        administration = USER_AUTH and (USER_ADMIN or USER_MOD)
        return (request.method in permissions.SAFE_METHODS
                or request.user == obj.author or administration)
