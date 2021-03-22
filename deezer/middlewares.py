from deezer.settings import ACCESS_TOKEN_HEADER


class AuthMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        jwt_value = request.auth
        if jwt_value:
            response[ACCESS_TOKEN_HEADER] = jwt_value
        return response
