from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from music.views import home, playlist, auth

urlpatterns = [
    path('', home.home_view, name='home'),
    path('login/', auth.index, name="auth.index"),
    path('login/authenticate/', auth.authenticate, name="auth.authenticate"),
    path('login/logout', auth.logout, name="auth.logout"),
    path('upload/', home.upload, name='upload'),
    path('playlist/create', playlist.create, name='playlist.create'),
    path('playlist/delete/<uuid:playlist_id>', playlist.delete, name='playlist.delete'),
    path('playlist/<uuid:playlist_id>/', playlist.index, name='playlist.index'),
]
