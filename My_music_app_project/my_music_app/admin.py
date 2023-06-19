from My_music_app_project.my_music_app.models import Profile, Album
from django.contrib import admin


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username']


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['album_name']
