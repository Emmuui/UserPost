from django.contrib import admin
from .models import UserAuth, ProfileUser, Category, Publication, Follower

admin.site.register(UserAuth)
admin.site.register(ProfileUser)
admin.site.register(Category)
admin.site.register(Publication)
admin.site.register(Follower)

