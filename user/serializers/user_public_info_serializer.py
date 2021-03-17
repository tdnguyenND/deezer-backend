from rest_framework.serializers import ModelSerializer

from user.models import User


class UserPublicInfoSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'picture']
