import requests
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from skills.models import ResourceLibrary, Skill, Specialization
from users.models import UserProfile, UserSkill
from api.v1.serializers import (DashboardSerializer, LevelSerializer,
                                LibrarySerializer, ShortUserSkillSerializer,
                                SkillDetailSerializer, SkillFrontSerializer,
                                UserCreateSkillSerializer, UserSkillSerializer,
                                UserUpdateSkillSerializer)

User = get_user_model()


class UserActivationView(APIView):
    """Обработка данных для активации юзера."""

    @staticmethod
    def get(request, uid, token):
        """Формирование POST-запроса активации юзера."""
        protocol = "https://" if request.is_secure() else "http://"
        post_url = f"{protocol}{request.get_host()}/api/v1/users/activation/"
        post_data = {"uid": uid, "token": token}
        result = requests.post(post_url, data=post_data)
        content = result.text
        return Response(content)


class MyUsersViewSet(UserViewSet):
    """Вьюсет пользователя."""


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    """Список всех навыков."""

    queryset = Skill.objects.all()
    serializer_class = SkillFrontSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'level',
        'specialization',
        'specialization__level_name')


class UserSkillViewSet(viewsets.ReadOnlyModelViewSet):
    """Навыки пользователя."""

    serializer_class = UserSkillSerializer

    def get_queryset(self):
        """Навыки текущего пользователя."""
        profile = get_object_or_404(UserProfile, user=self.request.user)
        return UserSkill.objects.filter(user_profile=profile)


class ShortUserSkillViewSet(viewsets.ModelViewSet):
    """Навыки пользователя сокращенный вид."""

    def get_serializer_class(self):
        """Получение класса сериализатора."""
        if self.request.method == "GET":
            return ShortUserSkillSerializer
        elif self.request.method == "POST":
            return UserCreateSkillSerializer
        elif self.request.method == "PATCH":
            return UserUpdateSkillSerializer

    def get_queryset(self):
        """Навыки текущего пользователя."""
        profile = get_object_or_404(UserProfile, user=self.request.user)
        return UserSkill.objects.filter(user_profile=profile)

    def perform_create(self, serializer):
        """Переопределение метода save."""
        profile = get_object_or_404(UserProfile, user=self.request.user)
        serializer.save(user_profile=profile)


class LevelViewSet(viewsets.ReadOnlyModelViewSet):
    """Список уровней должности."""

    queryset = Specialization.objects.all()
    serializer_class = LevelSerializer


class DashboardViewSet(viewsets.ReadOnlyModelViewSet):
    """Основаня страница пользователя."""

    serializer_class = DashboardSerializer
    pagination_class = None

    def get_queryset(self):
        """Навыки текущего пользователя."""
        return UserProfile.objects.filter(user=self.request.user)


class SkillDetail(generics.RetrieveAPIView):
    """Список всех навыков."""

    queryset = Skill.objects.all()
    serializer_class = SkillDetailSerializer


class LibraryViewSet(viewsets.ReadOnlyModelViewSet):
    """Список уровней должности."""

    queryset = ResourceLibrary.objects.all()
    serializer_class = LibrarySerializer
