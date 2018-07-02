from django.conf import settings
from django.contrib import messages
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from music.models import Playlist

@login_required
def index(request, playlist_id):
    """Index view for the playlist page"""
    playlist = get_object_or_404(Playlist, pk=playlist_id)

    return render(request, 'playlist.html', {
        'playlist': playlist,
        'media_url': request.get_host() + settings.MEDIA_URL
    })

# Create ModelForm  - https://docs.djangoproject.com/en/2.0/topics/forms/modelforms/
class NewPlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        fields = ['name', ]

@login_required
def create(request):
    form = NewPlaylistForm(request.POST)

    if form.is_valid():
        playlist = Playlist(name=request.POST['name'])
        playlist.save()

        messages.success(request, 'Playlist created')
        return redirect('home')

@login_required
def delete(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    playlist.delete()
    messages.success(request, 'Playlist Deleted')
    return redirect('home')
