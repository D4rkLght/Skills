from random import randint
import factory

from django.utils import timezone
from factory.django import DjangoModelFactory
from faker.providers import BaseProvider
from factory.fuzzy import FuzzyInteger, FuzzyChoice

from skills.models import ResourceLibrary, SkillGroup, Specialization, Skill

LOW_LIMIT = 5
HIGH_LIMIT = 15
MIN_RES_GEN = 1
MAX_RES_GEN = 5
RESOURCE_IDS = [x[0] for x in ResourceLibrary.RESOURCE_TYPE]
POST_LEVEL_IDS = [x[0] for x in Specialization.POST_LEVEL_NAMES]
SKILL_TYPE_IDS = [x[0] for x in Skill.SKILL_TYPE]
SKILL_LEVEL_IDS = [x[0] for x in Skill.SKILL_LEVEL]


class Provider(BaseProvider):
    """Provider для создания данных."""

    skills_name = ["Django", "Html", "Css", "Docker", "JS", "Python", "C++"]
    skills_group = ["Фрэймворки", "Языки программирования", "Коммуникабельность"]
    specialization = ['Разработчик', 'Дизайнер', 'Тестировщик', 'Аналитик', 'Продукт менеджер']
    
    def skill_names(self):
        """Названия навыков."""
        return self.random_element(self.skills_name)
    

    def skill_groups(self):
        """Группы навыков."""
        return self.random_element(self.skills_group)
    

    def specializations(self):
        """Сферы работы."""
        return self.random_element(self.specialization)


factory.Faker.add_provider(Provider)


class ResourceLibraryFactory(DjangoModelFactory):
    """Фабрика ресурсов библиотеки для тестирования проекта."""

    class Meta:
        model = ResourceLibrary

    type = FuzzyChoice(RESOURCE_IDS)
    description = factory.Faker("sentence")
    learning_time = FuzzyInteger(LOW_LIMIT, HIGH_LIMIT)
    url = factory.Faker("url")


class SkillGroupFactory(DjangoModelFactory):
    """Фабрика группы навыков для тестирования проекта."""

    class Meta:
        model = SkillGroup
        django_get_or_create = ("name",)

    name = factory.Faker("skill_groups")


class SpecializationFactory(DjangoModelFactory):
    """Фабрика cферы работы для тестирования проекта."""

    class Meta:
        model = Specialization
        django_get_or_create = ("name",)

    name = factory.Faker("specializations")
    code = FuzzyInteger(1, 1111)
    level_code = FuzzyInteger(1, 1111)
    level_name = FuzzyChoice(POST_LEVEL_IDS)


class SkillFactory(DjangoModelFactory):
    """Фабрика навыков для тестирования проекта."""

    class Meta:
        model = Skill
        django_get_or_create = ("name",)

    name = factory.Faker("skill_types")
    description = factory.Faker("sentence")
    specialization = factory.SubFactory(SpecializationFactory)
    group = factory.SubFactory(SkillGroupFactory)
    type = FuzzyChoice(SKILL_TYPE_IDS)
    level = FuzzyChoice(SKILL_LEVEL_IDS)
    code = FuzzyInteger(1, 1111)
    date_from = timezone.now()
    date_to = timezone.now()

    @factory.post_generation
    def resource_library(self, create, extracted, **kwargs):
        """Генерация resource_library."""
        if not create:
            return
        size = randint(MIN_RES_GEN, MAX_RES_GEN)
        if size <= ResourceLibrary.objects.count():
            for emp in range(1, size):
                self.resource_library.add(ResourceLibrary.objects.get(pk=emp))


def create_resources(amount: int = 1):
    """Создание ресурсов библиотеки для тестов программы."""
    ResourceLibraryFactory.create_batch(amount)


def create_skills(amount: int = 1):
    """Создание навыков для тестов программы."""
    SkillFactory.create_batch(amount)
