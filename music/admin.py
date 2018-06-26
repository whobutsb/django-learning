from django.contrib import admin
from music.models import track, playlist

admin.site.register(track.Track)
admin.site.register(playlist.Playlist)

# Register your models here.
