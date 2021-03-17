import datetime

import jwt
from rest_framework_jwt.serializers import jwt_payload_handler

from deezer import settings


def generate_refresh_token(user):
    payload = jwt_payload_handler(user)
    payload['exp'] = datetime.datetime.utcnow() + settings.JWT_AUTH.get('JWT_REFRESH_EXPIRATION_DELTA')
    access_token = jwt.encode(payload, settings.JWT_REFRESH_SECRET_KEY, algorithm='HS256').decode('utf-8')
    return access_token
