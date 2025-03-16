from rest_framework.routers import DefaultRouter
from django.urls import path, include

from basic_messenger.views import GroupChatViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r'profile', UserProfileViewSet)
router.register(r'group_chats', GroupChatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]