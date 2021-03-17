from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

from deezer.custom_jwt import obtain_token_pairs
from deezer.settings import logger

jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class SocialAuthentication(APIView):
    def authenticate(self, request):
        """
        Authenticate user from social credentials
        :param request:
        :return: user that authenticated
        """
        raise NotImplementedError('Not implement authenticate() function')

    def post(self, request, *args, **kwargs):
        user = self.authenticate(request)
        access_token, refresh_token = obtain_token_pairs(user)
        response_data = jwt_response_payload_handler(access_token=access_token, user=user)
        response_data['refresh_token'] = refresh_token
        return Response(response_data)
