from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet


class AuthenticatedGenericViewSet(GenericViewSet):
    permission_classes = [IsAuthenticated]
