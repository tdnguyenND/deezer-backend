import jwt
from rest_framework_jwt.serializers import jwt_payload_handler

from deezer import settings


def generate_access_token(user):
    payload = jwt_payload_handler(user)
    access_token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm='HS256').decode('utf-8')
    return access_token
