from deezer.custom_jwt.generate_access_token import generate_access_token
from deezer.custom_jwt.generate_refresh_token import generate_refresh_token


def obtain_token_pairs(user):
    return generate_access_token(user), generate_refresh_token(user)
