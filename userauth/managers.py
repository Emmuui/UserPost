from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra):

        if email:
            email = self.normalize_email(email)
            if not username:
                username=email

        user = self.model(
            username=username,
            email=email,
            **extra,
        )

        if extra.get('is_superuser'):
            user = self.model(
                username=username,
                **extra
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def _create_user(self, username, email, password=None, **extra):
        extra.setdefault('is_superuser', False)
        return self.create_user(username=username, email=email, password=password, **extra)

    def create_superuser(self, username, password=None, **extra):
        extra.setdefault('is_superuser', True)
        extra.setdefault('is_staff', True)
        extra.setdefault('is_active', True)

        return self.create_user(
            username=username,
            password=password,
            **extra
        )