from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

from skills.models import Specialization, Skill


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
    current_specialization = models.ForeignKey(Specialization,
                                       related_name='user_specialization',
                                       verbose_name='Текущий уровень',
                                       on_delete=models.PROTECT,)
    skills = models.ManyToManyField(Skill, through='UserSkill',
                                    verbose_name='Скиллы пользователя',
                                    related_name='user_skills')
    goal_specialization = models.ForeignKey(Specialization,
                                        verbose_name='Желаемый уровень',
                                        related_name='user_goal',
                                        on_delete=models.SET_DEFAULT,
                                        default=0)
    

    class Meta:
        verbose_name = 'Данные пользователя'
        verbose_name_plural = 'Данные пользователя'

    def __str__(self):
        return self.user.username


class UserSkill(models.Model):
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

