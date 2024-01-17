from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from.models import Song

# Create your views here.
def songlist(request):
    songs=Song.objects.all()
    return render(request,'songlist.html',{'songs':songs})


def play(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'play.html', {'song':song})
