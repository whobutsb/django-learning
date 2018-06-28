from django.conf import settings
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

@login_required
def create(request):
    form = NewPlaylistForm(request.POST)

    if form.is_valid():
        playlist = Playlist(name=request.POST['name'])
        playlist.save()

        messages.success(request, 'Playlist created')
        return redirect('home')
