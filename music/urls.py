from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from music.views import home

urlpatterns = [
    path('', home.home_view, name='home'),
    path('upload/', home.upload, name='upload'),
    path('playlist/create', home.playlist_create, name='playlist_create'),
]
