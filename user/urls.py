from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.view_sets import UserViewSet

user_router = DefaultRouter()
user_router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(user_router.urls)),
]
