from django.db import models


class ResourceLibrary(models.Model):
    RESOURCE_TYPE = [('course', 'Курс'),
            ('article', 'Статья'),
            ('podcast', 'Подкаст'),
            ('other', 'Другое')]
    
    type = models.CharField(max_length=8, choices=RESOURCE_TYPE)
    description = models.TextField()
    learning_time = models.IntegerField()
    url = models.URLField()

    class Meta:
        verbose_name = 'Библиотека ресурсов'
        verbose_name_plural = 'Библиотеки ресурсов'

    def __str__(self):
        return self.type
    

class SkillGroup(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Группа навыка'
        verbose_name_plural = 'Группы навыков'

    def __str__(self):
        return self.name

   
class Specialization(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    code = models.IntegerField()

    class Meta:
        verbose_name = 'Сфера работы'
        verbose_name_plural = 'Сферы работы'

    def __str__(self):
        return self.name
    

class PostLevel(models.Model):
    POST_LEVEL_NAMES = [('none', 'Не знаю'),
                        ('jun', 'Junior'),
                        ('mid', 'Middle'),
                        ('mid+', 'Middle+'),
                        ('sen', 'Senior'),
                        ('sen+', 'Senior+')]

    specialization = models.ForeignKey(Specialization,
                                       verbose_name='Сфера работы',
                                       related_name='post_specialization',
                                       on_delete=models.CASCADE)
    code = models.IntegerField()
    name = models.CharField(max_length=4, choices=POST_LEVEL_NAMES)

    class Meta:
        verbose_name = 'Уровень должности'
        verbose_name_plural = 'Уровни должности'

    def __str__(self):
        return f'{self.name}, {self.specialization.name}'


class Skill(models.Model):
    SKILL_TYPE = [('soft', 'Софт скилл'), ('hard','Хард скилл')]

    name = models.CharField(max_length=50, verbose_name='Название навыка')
    description = models.TextField()
    specialization = models.ForeignKey(Specialization,
                                       verbose_name='Сфера работы',
                                       related_name='skill_specialization',
                                       on_delete=models.PROTECT)
    group = models.ForeignKey(SkillGroup,
                              verbose_name='Группа навыка',
                              related_name='skill_group',
                              on_delete=models.PROTECT)
    type = models.CharField(max_length=4, choices=SKILL_TYPE, verbose_name='Тип навыка')
    post_level = models.ForeignKey(PostLevel,
                                   verbose_name='Уровень должности',
                                   related_name='post_level', 
                                   on_delete=models.SET_NULL,
                                   null=True, blank=True)
                                 #  limit_choices_to={'specialization': specialization})
    code = models.IntegerField()

    date_from = models.DateField(verbose_name='Дата начала действия навыка')
    date_to = models.DateField(verbose_name='Дата окончания действия навыка', default=None, null=True, blank=True)
    resource_library = models.ManyToManyField(ResourceLibrary,
                                               verbose_name='Библиотека ресурсов',
                                               related_name='resource_library')

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.name
