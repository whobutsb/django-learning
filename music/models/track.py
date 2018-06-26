import uuid
from django.db import models

class Track(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, null=False)
    artist = models.CharField(max_length=200, null=False)
    album = models.CharField(max_length=200, null=False)
    year = models.IntegerField(null=False)
    file_path = models.FileField(upload_to='tracks/')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.artist + ' - ' + self.title
