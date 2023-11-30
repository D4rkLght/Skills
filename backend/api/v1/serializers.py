from rest_framework import serializers

from skills.models import Skill
from users.models import UserSkill


class SkillSerializer(serializers.ModelSerializer):
    """Добавить описание."""

    class Meta:
        model = Skill
        fields = "__all__"


class UserSkillSerializer(serializers.ModelSerializer):
    """Добавить описание."""

    skill = SkillSerializer()

    class Meta:
        model = UserSkill
        fields = ("id", "status", "date_from", "date_to", "skill")
