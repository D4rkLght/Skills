from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
#from django_filters.rest_framework import DjangoFilterBackend

from users.models import UserSkill
from skills.models import Skill
from api.serializers import (SkillSerializer, UserSkillSerializer)


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
 #   pagination_class = PageNumberPagination
 #   filter_backends = (DjangoFilterBackend,)
 #   filterset_fields = ('category',)


class UserSkillViewSet(viewsets.ModelViewSet):
    queryset = UserSkill.objects.all()
    serializer_class = UserSkillSerializer