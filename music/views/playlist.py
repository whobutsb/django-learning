from django.shortcuts import render, redirect, get_object_or_404

from music.models import Playlist

def index(request, playlist_id):
    """Index view for the playlist page"""
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    return render(request, 'playlist.html', { 'playlist': playlist })

def create(request):
    form = NewPlaylistForm(request.POST)

    if form.is_valid():
        playlist = Playlist(name=request.POST['name'])
        playlist.save()

        messages.success(request, 'Playlist created')
        return redirect('home')
