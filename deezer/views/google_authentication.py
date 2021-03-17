from google.auth.transport import requests
from google.oauth2 import id_token

from deezer import settings
from deezer.settings import logger
from deezer.views.social_authentication import SocialAuthentication
from user.constant import AccountType
from user.models import User


class GoogleAuthenticationAPIView(SocialAuthentication):
    def authenticate(self, request):
        client_id_token = request.data.get('token')
        google_user = id_token.verify_oauth2_token(client_id_token, requests.Request(), settings.GOOGLE_CLIENT_ID)

        related_id = google_user.get('sub')
        name = google_user.get('name')
        email = google_user.get('email')
        picture = google_user.get('picture')
        user, created = User.objects.get_or_create(related_id=related_id, account_type=AccountType.GOOGLE,
                                                   defaults={'name': name, 'email': email, 'picture': picture})
        return user
