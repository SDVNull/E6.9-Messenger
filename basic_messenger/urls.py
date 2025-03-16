from rest_framework.routers import DefaultRouter
from django.urls import path, include
from basic_messenger.views import GroupChatViewSet, RegistrationAPIView, UserProfileViewSet
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r"profile", UserProfileViewSet)
router.register(r"group_chats", GroupChatViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # url для токенов доступа (access) и обновления (refresh)
    # время жизни токенов 1 час и 7 дней соответвенно (указано в settings.py)
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # url для регистрации и входа
    path("api/register/", RegistrationAPIView.as_view(), name="register"), # api регистрации
    path("login/", TemplateView.as_view(template_name="login.html")), # вход (форма)
    path("register/", TemplateView.as_view(template_name="register.html")), # регистрация (форма)
]
