from rest_framework import serializers

from skills.models import Skill, SkillGroup, ResourceLibrary
from users.models import UserSkill, Specialization, UserProfile


class GroupSerializer(serializers.ModelSerializer):
    """Отображение группы."""

    class Meta:
        model = SkillGroup
        fields = "__all__"


class SpecializationDashbordSerializer(serializers.ModelSerializer):
    """Отображение сферы работы в Дашборде."""

    class Meta:
        model = Specialization
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    """Список всех навыков."""

    group = GroupSerializer()
    specialization = SpecializationDashbordSerializer()

    class Meta:
        model = Skill
        fields = ('id', 'code', 'name', 'level', 'group', 'specialization')


class UserSkillSerializer(serializers.ModelSerializer):
    """Навыки пользователя."""

    skill = SkillSerializer()

    class Meta:
        model = UserSkill
        fields = ("id", "status", "date_from", "date_to", "skill",)


class LevelSerializer(serializers.ModelSerializer):
    """Список всех уровней должности."""

    class Meta:
        model = Specialization
        fields = "__all__"


class ResourceLibrarySerializer(serializers.ModelSerializer):
    """Отображение библиотек на дашборде."""
    
    class Meta:
        model = ResourceLibrary
        fields = "__all__"


class SkillDashbordSerializer(serializers.ModelSerializer):
    """Детальная информация о навыках для дашборда."""

    resource_library = ResourceLibrarySerializer(many=True)

    class Meta:
        model = Skill
        fields = ("id", "name", "description", "code", "resource_library")


class UserSkillDashbordSerializer(serializers.ModelSerializer):
    """Список всех навыков для Дашборда."""

    skill = SkillDashbordSerializer()

    class Meta:
        model = UserSkill
        fields = ("id", "status", "date_from", "date_to", "skill")


class DashboardSerializer(serializers.ModelSerializer):
    """Дашборд пользователя."""

    current_specialization = SpecializationDashbordSerializer(read_only=True)
    goal_specialization = SpecializationDashbordSerializer(read_only=True)
    skills = UserSkillDashbordSerializer(source='skill_user', many=True)

    class Meta:
        model = UserProfile
        fields = (
            "id",
            "current_specialization",
            "goal_specialization",
            "skills")


class SpecializationShortSerializer(serializers.ModelSerializer):
    """Краткое отображение сферы работы."""

    class Meta:
        model = Specialization
        fields = ('id', 'name')


class SkillDetailSerializer(serializers.ModelSerializer):
    """Детальная информация о навыке."""

    resource_library = ResourceLibrarySerializer(many=True)
    specialization = SpecializationShortSerializer()

    class Meta:
        model = Skill
        fields = "__all__"
        fields = (
            "id",
            "resource_library",
            "name",
            "description",
            "level",
            "code",
            "specialization")


class LibrarySerializer(serializers.ModelSerializer):
    """Отображение отдельно библиотек."""

    skills = SkillSerializer(many=True, source='resource_library')

    class Meta:
        model = ResourceLibrary
        fields = (
            "id",
            "type",
            "description",
            "learning_time",
            "url",
            "skills",
        )
