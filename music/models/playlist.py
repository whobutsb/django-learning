import uuid
from django.db import models
from django.urls import reverse

from .track import Track

class Playlist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    tracks = models.ManyToManyField(Track)

    def get_absolute_url(self):
        return reverse('playlist.index', kwargs={'playlist_id': self.id})


