from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView


class AdminAPIView(APIView):
    permission_classes = [IsAdminUser]
