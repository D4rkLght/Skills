from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

from skills.models import Specialization, Skill, PostLevel


#User = get_user_model()

class User(AbstractUser):
    trecker_id = models.CharField(unique=True, verbose_name='ID Яндекс Трекера', max_length=200)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
    

class UserProfile(models.Model):
    user = models.ForeignKey(User,
                             verbose_name="Пользователь",
                             related_name="profile_user",
                             on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization,
                                       related_name='user_specialization',
                                       verbose_name='Сфера работы',
                                       on_delete=models.PROTECT,)
    skills = models.ManyToManyField(Skill, through='UserSkills',
                                    verbose_name='Скиллы пользователя',
                                    related_name='user_skills')
    current_post_level = models.ForeignKey(PostLevel,
                                           verbose_name='Текущий уровень должности', 
                                           related_name='current_level',
                                           on_delete=models.PROTECT,
                                           default=0)
    goal_post_level = models.ForeignKey(PostLevel,
                                        verbose_name='Желаемый уровень должности',
                                        related_name='goal_level',
                                        on_delete=models.SET_DEFAULT,
                                        default=0)
    

    class Meta:
        verbose_name = 'Данные пользователя'
        verbose_name_plural = 'Данные пользователя'

    def __str__(self):
        return self.user.username


class UserSkills(models.Model):
    SKILL_STATUS = [('start', 'Добавлен'), ('process', 'В процессе'), ('done', 'Изучен')]

    user_profile = models.ForeignKey(UserProfile,
                             verbose_name="Пользователь",
                             related_name="skill_user",
                             on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill,
                              related_name='skill',
                              verbose_name='Навык',
                              on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=8, choices=SKILL_STATUS)
    date_from = models.DateField(verbose_name='Дата начала действия навыка', default=None, null=True, blank=True)
    date_to = models.DateField(verbose_name='Дата окончания действия навыка', default=None, null=True, blank=True)

    class Meta:
        verbose_name = 'Скилл пользователя'
        verbose_name_plural = 'Скиллы пользователя'

    def __str__(self):
        return f'Пользователь {self.user_profile}'

