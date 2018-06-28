import eyed3
import datetime
from django import forms
from django.forms import ModelForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms.utils import ValidationError

from music.models import Track, Playlist

# Formsets - https://docs.djangoproject.com/en/2.0/topics/forms/formsets/
class TrackForm(forms.Form):
    file_path = forms.FileField(label='Select a MP3 file',  help_text='max 42MB')

# Create ModelForm  - https://docs.djangoproject.com/en/2.0/topics/forms/modelforms/
class NewPlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        fields = ['name', ]

@login_required
def home_view(request):
    return render(request, 'home.html', {
        'upload_form': TrackForm(),
        'playlist_form': NewPlaylistForm(),
        'playlists': Playlist.objects.all(),
    })

# https://simpleisbetterthancomplex.com/tutorial/2016/11/22/django-multiple-file-upload-using-ajax.html
# https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html
# https://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example
@login_required
def upload(request):
    form = TrackForm(request.POST, request.FILES)
    if form.is_valid():
        # get the mp3 data from the temp path
        try:
            mp3 = eyed3.load(request.FILES['file_path'].file.name)
        except Exception as e:
            messages.error(request, 'This is not a mp3 file')
            return redirect('home')

        # set the track data
        track = Track(
            artist = mp3.tag.artist,
            title = mp3.tag.title,
            album = mp3.tag.album,
            year = mp3.tag.release_date.year,
            file_path = request.FILES['file_path']
        )
        # make sure it will process
        try:
            track.full_clean()
        except ValidationError as e:
            messages.error(request, 'Error validating: ' + '; '.join(e.messages))
            return redirect('home')

        messages.success(request, 'MP3 Track uploaded')
        track.save()
        return redirect('home')

