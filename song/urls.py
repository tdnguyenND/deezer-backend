from django.urls import path, include
from rest_framework.routers import DefaultRouter

from song.view_sets import SongViewSet

song_router = DefaultRouter()
song_router.register(r'', SongViewSet)

urlpatterns = [
    path('song/', include(song_router.urls)),
]
