from django.contrib import admin
from accounts.models import Users, ProfileUser


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(ProfileUser)
class ProfileUseraAdmin(admin.ModelAdmin):
    pass
