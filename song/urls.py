from django.urls import path, include
from rest_framework.routers import DefaultRouter

from song.view_sets import SongViewSet, PlaylistViewSet

song_router = DefaultRouter()
song_router.register(r'', SongViewSet)

playlist_router = DefaultRouter()
playlist_router.register(r'', PlaylistViewSet)

urlpatterns = [
    path('song/', include(song_router.urls)),
    path('playlist/', include(playlist_router.urls))
]
