from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from music.views import home

urlpatterns = [
    path('', home.home_view, name='home'),
    path('upload/', home.upload, name='upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, docment_root=settings.MEDIA_ROOT)
