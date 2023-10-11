from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class UserProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class CustomizedUserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

admin.site.register(SliderImage)
admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)