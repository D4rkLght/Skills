from django.db import models
from django.contrib.auth import get_user_model

from skills.models import Goal, Level


User = get_user_model()


class UserSkills(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", related_name="user_skills")
    level = models.ForeignKey(Level, related_name='user_level', verbose_name="Уровень")
    goal = models.ForeignKey(Goal, related_name="user_goal", verbose_name='Цель')
    grade = models.IntegerField()

    class Meta:
        verbose_name = 'Скилл пользователя'
        verbose_name_plural = 'Скиллы пользователя'

    def __str__(self):
        return f'Пользователь {self.user} текцший уровень: {self.level}. Цель: {self.goal} '
