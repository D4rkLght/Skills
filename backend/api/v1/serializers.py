from rest_framework import serializers
from django.db.models import Q

from skills.models import Skill, SkillGroup, ResourceLibrary
from users.models import UserSkill, Specialization, UserProfile, UserResources


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

    resource_library = serializers.SerializerMethodField()

    class Meta:
        model = Skill
        fields = ("id", "name", "description", "code", "resource_library")


    def get_resource_library(self, obj):
        queryset = obj.resource_library.all()[:1]
        return ResourceLibrarySerializer(queryset, many=True).data


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
    skills = serializers.SerializerMethodField()
    user_learning_time = serializers.SerializerMethodField()
    user_skills_count = serializers.SerializerMethodField()
    user_hard_skills_count = serializers.SerializerMethodField()
    user_soft_skills_count = serializers.SerializerMethodField()
    percent_studied = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = (
            "id",
            "current_specialization",
            "goal_specialization",
            "user_learning_time",
            "user_skills_count",
            "user_hard_skills_count",
            "user_soft_skills_count",
            "percent_studied",
            "skills",
            )


    def get_skills(self, obj):
        queryset = obj.skill_user.all()[:6]
        return UserSkillDashbordSerializer(queryset, many=True).data


    def get_user_learning_time(self, obj):
        queryset = UserResources.objects.filter(profile=obj, status='done')
        count_time = 0
        for item in queryset:
            count_time += item.resource.learning_time
        return count_time
    

    def get_user_skills_count(self, obj):
        return obj.skills.count()
    
    
    def get_user_hard_skills_count(self, obj):
        return obj.skills.filter(type='hard').count()

    
    def get_user_soft_skills_count(self, obj):
        return obj.skills.filter(type='soft').count()
    
            
    def get_percent_studied(self, obj):
        studied_count = len(UserResources.objects.filter(profile=obj, status='done'))
        queryset = Skill.objects.filter(specialization=obj.goal_specialization)
        goal_studied_count = 0
        for item in queryset:
            goal_studied_count += item.resource_library.count()
        return int(studied_count*100/goal_studied_count)


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
