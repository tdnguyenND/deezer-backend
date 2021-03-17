from rest_framework.decorators import action
from rest_framework.response import Response

from deezer.view_sets import AuthenticatedGenericViewSet
from user.models import User
from user.serializers import UserPublicInfoSerializer, UserSerializer


class UserViewSet(AuthenticatedGenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserPublicInfoSerializer

    @action(methods=['GET'], detail=False, url_path='self-info')
    def get_self_info(self, request):
        user = request.user
        response_data = UserSerializer(user).data
        return Response(response_data)
