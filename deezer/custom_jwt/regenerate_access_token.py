import datetime

import jwt

from deezer import settings
from deezer.custom_jwt.generate_access_token import generate_access_token
from user.models import User


def regenerate_access_token(refresh_token):
    payload = jwt.decode(refresh_token, key=settings.JWT_REFRESH_SECRET_KEY)
    user_id = payload.get('user_id')
    user = User.objects.get(id=user_id)
    exp = payload.get('exp')
    exp_date = datetime.datetime.utcfromtimestamp(exp)
    if exp_date > datetime.datetime.utcnow():
        return generate_access_token(user)
    else:
        raise jwt.ExpiredSignature
