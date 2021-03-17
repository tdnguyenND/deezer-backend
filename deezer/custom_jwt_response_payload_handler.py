from user.serializers import UserSerializer


def custom_jwt_response_handler(access_token, user, refresh_token=None):
    return {
        'access_token': access_token,
        'user': UserSerializer(user).data,
        'refresh_token': refresh_token
    }
