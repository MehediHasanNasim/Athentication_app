from django.contrib import admin
from .models import ProfilePicture
# Register your models here.


@admin.register(ProfilePicture)
class ProfilePictureAdmin(admin.ModelAdmin):
    list_display = ('user', 'image')