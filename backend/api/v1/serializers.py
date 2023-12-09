from rest_framework import serializers
from django.shortcuts import get_object_or_404
from skills.models import ResourceLibrary, Skill, SkillGroup
from users.models import Specialization, UserProfile, UserResources, UserSkill


class GroupSerializer(serializers.ModelSerializer):
    """Отображение группы."""

    class Meta:
        model = SkillGroup
        fields = ('id','name')


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
        fields = ('id', 'name', 'level', 'group', 'specialization')


class ResourceLibrarySerializer(serializers.ModelSerializer):
    """Отображение библиотек на дашборде."""

    learning_status = serializers.SerializerMethodField()
    class Meta:
        model = ResourceLibrary
        fields = ("id", "type", "description",
                  "learning_time", "url", "learning_status")


    def get_learning_status(self, obj):
        """Получение статуса изучения ресурса."""
        if not self.context:
            return None
        profile = UserProfile.objects.get(user=self.context['request'].user)
        current_resource = UserResources.objects.filter(
            resource=obj, profile=profile)
        if current_resource:
            return current_resource[0].status == 'done'
        return False


class SkillFrontSerializer(serializers.ModelSerializer):
    """Список всех навыков удобный фронту."""

    group = GroupSerializer()
    resource_library = ResourceLibrarySerializer(many=True)
    level = serializers.CharField(source='get_level_display')

    class Meta:
        model = Skill
        fields = ('id', 'name', 'level', 'group',
                  'description', 'type', 'resource_library')


class UserSkillSerializer(serializers.ModelSerializer):
    """Навыки пользователя."""

    skill = SkillFrontSerializer()

    class Meta:
        model = UserSkill
        fields = ("skill",)


class ProfileSerializer(serializers.ModelSerializer):
    """Создание профайла пользователя."""

    class Meta:
        model = UserProfile
        fields = ('current_specialization', 'goal_specialization', 'skills')


    def validate(self, data):
        """Проверка, что такого у пользователя еще нет профайла."""
        profile = UserProfile.objects.filter(
            user=self.context['request'].user).exists()
        if profile:
            raise serializers.ValidationError(
                'Профайл уже существует!')
        return data

    def create(self, validated_data):
        """Переопределение метода create."""
        skills = self.initial_data.pop('skills')
        profile = UserProfile.objects.create(**validated_data)
        for status in skills:
            for id in skills[status]:
                current_skill = get_object_or_404(Skill, id=id)
                UserSkill.objects.create(
                    skill=current_skill, user_profile=profile, status=status)
        return validated_data


class LevelSerializer(serializers.ModelSerializer):
    """Список всех уровней должности."""

    class Meta:
        model = Specialization
        fields = "__all__"


class SkillDashbordSerializer(serializers.ModelSerializer):
    """Детальная информация о навыках для дашборда."""

    resource_library = serializers.SerializerMethodField()

    class Meta:
        model = Skill
        fields = ("id", "name", "description", "code", "resource_library")

    def get_resource_library(self, obj):
        """получение всех ресурсов пользователя."""
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
        """Получение списка софт скиллов."""
        queryset = obj.skill_user.all()[:6]
        return UserSkillDashbordSerializer(queryset, many=True).data

    def get_user_learning_time(self, obj):
        """Получение суммарного времени обучения."""
        queryset = UserResources.objects.filter(profile=obj, status='done')
        count_time = 0
        for item in queryset:
            count_time += item.resource.learning_time
        return count_time

    def get_user_skills_count(self, obj):
        """Получение количества скиллов."""
        return obj.skills.count()

    def get_user_hard_skills_count(self, obj):
        """Получение количества хард скиллов."""
        return obj.skills.filter(type='hard').count()

    def get_user_soft_skills_count(self, obj):
        """Получение количества софт скиллов."""
        return obj.skills.filter(type='soft').count()

    def get_percent_studied(self, obj):
        """Получение процента изученных материалов."""
        studied_count = len(
            UserResources.objects.filter(
                profile=obj, status='done'))
        queryset = Skill.objects.filter(specialization=obj.goal_specialization)
        goal_studied_count = 0
        for item in queryset:
            goal_studied_count += item.resource_library.count()
        if goal_studied_count:
            return int(studied_count * 100 / goal_studied_count)
        return 100


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


class ShortUserSkillSerializer(serializers.ModelSerializer):
    """Навыки пользователя только название."""

    skill = serializers.StringRelatedField()

    class Meta:
        model = UserSkill
        fields = ("skill",)


class UserCreateSkillSerializer(serializers.ModelSerializer):
    """Создание навыка пользователя."""

    class Meta:
        model = UserSkill
        fields = ("skill", "status")

    def validate(self, data):
        """Проверка, что такого скилла у пользователя еще нет."""
        profile = UserProfile.objects.get(user=self.context['request'].user)
        if UserSkill.objects.filter(
                user_profile=profile,
                skill=data['skill']).exists():
            raise serializers.ValidationError(
                'Такой навык уже существует!')
        return data


class UserUpdateSkillSerializer(serializers.ModelSerializer):
    """Изменение статуса навыка пользователя."""

    class Meta:
        model = UserSkill
        fields = ("status",)
