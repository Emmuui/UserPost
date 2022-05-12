from django.dispatch import receiver
from djoser.signals import user_registered

from userauth.models import ProfileUser


@receiver(user_registered, dispatch_uid="create_profile")
def create_profile(sender, user, request, **kwargs):

    data = request.data

    ProfileUser.objects.create(
        user=user,
        first_name=data.get("name", ""),
        second_name=data.get("surname", "")
    )