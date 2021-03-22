from django.urls import path, include

from deezer.views import FacebookAuthenticationAPIView, GoogleAuthenticationAPIView
from user.urls import urlpatterns as user_urls
from song.urls import urlpatterns as song_urls

urlpatterns = [
    path('facebook-authentication/', FacebookAuthenticationAPIView.as_view()),
    path('google-authentication/', GoogleAuthenticationAPIView.as_view()),
    path('user/', include(user_urls)),
    path('song/', include(song_urls)),
]
