from django.urls import path
from . import views

urlpatterns=[
    path("",views.songlist,name='home'),
    path('play/<int:song_id>/',views.play,name="play")
]
