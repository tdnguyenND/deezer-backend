import json

from open_facebook import OpenFacebook

from deezer.settings import logger
from deezer.views.social_authentication import SocialAuthentication
from user.constant import AccountType
from user.models import User


class FacebookAuthenticationAPIView(SocialAuthentication):
    def authenticate(self, request):
        access_token = request.data.get('token')
        facebook = OpenFacebook(access_token)
        public_data = facebook.get('me', fields='id,name,email,picture')
        related_id = public_data.get('id')
        name = public_data.get('name')
        email = public_data.get('email')
        picture = public_data.get('picture')['data']['url']
        user, created = User.objects.get_or_create(related_id=related_id, account_type=AccountType.FACEBOOK,
                                                   defaults={'name': name, 'email': email, 'picture': picture})
        return user
