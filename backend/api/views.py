from api.serializers import SkillSerializer, UserSkillSerializer
from rest_framework import viewsets

from skills.models import Skill
from users.models import UserSkill

# from rest_framework.pagination import PageNumberPagination
# from django_filters.rest_framework import DjangoFilterBackend


class SkillViewSet(viewsets.ModelViewSet):
    """Добавить описание."""

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


#   pagination_class = PageNumberPagination
#   filter_backends = (DjangoFilterBackend,)
#   filterset_fields = ('category',)


class UserSkillViewSet(viewsets.ModelViewSet):
    """Добавить описание."""

    queryset = UserSkill.objects.all()
    serializer_class = UserSkillSerializer
