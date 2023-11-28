import requests
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
#from django_filters.rest_framework import DjangoFilterBackend

from users.models import UserSkill, UserProfile
from skills.models import Skill
from api.v1.serializers import (SkillSerializer, UserSkillSerializer)


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

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
 #   pagination_class = PageNumberPagination
 #   filter_backends = (DjangoFilterBackend,)
 #   filterset_fields = ('category',)


class UserSkillViewSet(viewsets.ModelViewSet):
    serializer_class = UserSkillSerializer

    def get_queryset(self):
        profile = get_object_or_404(UserProfile, user=self.request.user)
        return UserSkill.objects.filter(user_profile=profile)
