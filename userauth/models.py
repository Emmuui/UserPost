from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.conf import settings
from django.core.validators import FileExtensionValidator

from .managers import UserManager
from .services import upload_to_userprofile, upload_image_publication


class UserAuth(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )

    username = models.CharField(verbose_name='username', max_length=150, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name='Date joined', auto_now_add=True)

    is_verified = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


class ProfileUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name='first name', max_length=150, null=True, blank=True)
    second_name = models.CharField(verbose_name='second name', max_length=150, null=True, blank=True)
    image = models.ImageField(verbose_name='Image', default='default_image.png',
                              upload_to=upload_to_userprofile,
                              validators=[FileExtensionValidator(allowed_extensions=['jpg'])],
                              null=True, blank=True)
    date_of_birth = models.DateField(verbose_name='Date of birth', null=True, blank=True)
    description = models.TextField(verbose_name='Description', max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = 'ProfileUser'
        verbose_name_plural = 'ProfileUsers'

    def __str__(self):
        return self.user.username


class Follower(models.Model):
    user = models.ForeignKey(UserAuth, related_name='user', on_delete=models.CASCADE)
    follower = models.ForeignKey(UserAuth, related_name='follower', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Follower'
        verbose_name_plural = 'Followers'

    def __str__(self):
        return f'{self.follower} подписался на {self.user}'


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
       return self.name


class Publication(models.Model):
    user = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to=upload_image_publication,
                              validators=[FileExtensionValidator(allowed_extensions=['jpg'])],
                              null=True, blank=True)
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modify = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'

    def __str__(self):
        return f'{self.user} опубликовал {self.title}'