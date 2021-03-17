from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView


class AuthenticatedAPIView(APIView):
    permission_classes = [IsAdminUser]
