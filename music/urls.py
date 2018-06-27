from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from music.views import home, playlist

urlpatterns = [
    path('', home.home_view, name='home'),
    path('upload/', home.upload, name='upload'),
    path('playlist/create', playlist.create, name='playlist.create'),
    path('playlist/<uuid:playlist_id>/', playlist.index, name='playlist.index'),
]
