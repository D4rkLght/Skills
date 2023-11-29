from rest_framework import serializers
from skills.models import Skill
from users.models import UserSkill


class SkillSerializer(serializers.ModelSerializer):
    """Придумать докстринг."""

    class Meta:
        model = Skill
        fields = "__all__"


class UserSkillSerializer(serializers.ModelSerializer):
    """Придумать докстринг."""

    skill = SkillSerializer()

    class Meta:
        model = UserSkill
        fields = "__all__"
