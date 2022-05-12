from .models import UserAuth
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend


class AuthBackend(object):
    supports_object_permissions = True
    supports_anonymous_user = False
    supports_inactive_user = False

    def get_user(self, id):
        try:
            return UserAuth.objects.get(pk=id)
        except UserAuth.DoesNotExist:
            return None

    def authenticate(self, request, username, password):

        try:
            user = UserAuth.objects.get(
                Q(username=username) | Q(email=username)
            )

        except UserAuth.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        else:
            return None
