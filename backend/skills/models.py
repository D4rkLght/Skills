from django.db import models


class ResourceLibrary(models.Model):
    """Ресурсы библиотеки."""

    RESOURCE_TYPE = [
        ("course", "Курс"),
        ("article", "Статья"),
        ("podcast", "Подкаст"),
        ("other", "Другое"),
    ]

    type = models.CharField(max_length=8, choices=RESOURCE_TYPE)
    description = models.TextField()
    learning_time = models.IntegerField()
    url = models.URLField()

    class Meta:
        verbose_name = "Библиотека ресурсов"
        verbose_name_plural = "Библиотеки ресурсов"

    def __str__(self):
        return self.type


class SkillGroup(models.Model):
    """Группы навыков."""

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Группа навыка"
        verbose_name_plural = "Группы навыков"

    def __str__(self):
        return self.name


class Specialization(models.Model):
    """Профессии."""

    POST_LEVEL_NAMES = [
        ("none", "Не знаю"),
        ("jun", "Junior"),
        ("mid", "Middle"),
        ("mid+", "Middle+"),
        ("sen", "Senior"),
        ("sen+", "Senior+"),
    ]

    name = models.CharField(max_length=255, verbose_name="Название")
    code = models.IntegerField()
    level_code = models.IntegerField()
    level_name = models.CharField(max_length=4, choices=POST_LEVEL_NAMES)

    class Meta:
        verbose_name = "Сфера работы"
        verbose_name_plural = "Сферы работы"

    def __str__(self):
        return f"{self.name} {self.level_name}"


class Skill(models.Model):
    """Навыки."""

    SKILL_TYPE = [("soft", "Софт скилл"),
                  ("hard", "Хард скилл")]

    SKILL_LEVEL = [("start", "Базовый"),
                   ("middle", "Средний"),
                   ("senior", "Продвинутый")]

    name = models.CharField(max_length=50, verbose_name="Название навыка")
    description = models.TextField()
    specialization = models.ForeignKey(
        Specialization,
        verbose_name="Сфера работы",
        related_name="skill_specialization",
        on_delete=models.PROTECT,
    )
    group = models.ForeignKey(
        SkillGroup,
        verbose_name="Группа навыка",
        related_name="skill_group",
        on_delete=models.PROTECT,
    )
    type = models.CharField(
        max_length=4, choices=SKILL_TYPE, verbose_name="Тип навыка"
    )
    level = models.CharField(
        max_length=6, choices=SKILL_LEVEL, verbose_name="Уровень навыка"
    )
    code = models.IntegerField()
    date_from = models.DateField(verbose_name="Дата начала действия навыка")
    date_to = models.DateField(
        verbose_name="Дата окончания действия навыка",
        default=None,
        null=True,
        blank=True,
    )
    resource_library = models.ManyToManyField(
        ResourceLibrary,
        verbose_name="Библиотека ресурсов",
        related_name="resource_library",
    )

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.name
