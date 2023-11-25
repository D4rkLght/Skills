from django.db import models

from users.models import User


class SoftSkill(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    slug = models.CharField(max_length=50)
    status = models.BinaryField(default=0, verbose_name="Наличие")

    class Meta:
        verbose_name = 'Софт скил'
        verbose_name_plural = 'Софт скиллы'

    def __str__(self):
        return self.name
    

class HardSkill(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    slug = models.CharField(max_length=150)
    status = models.BinaryField(default=0, verbose_name="Наличие")

    class Meta:
        verbose_name = 'Софт скил'
        verbose_name_plural = 'Софт скиллы'

    def __str__(self):
        return self.name


class Level(models.Model):
    soft_skill = models.ForeignKey(SoftSkill, verbose_name='Софт скилл', related_name='soft_skill')
    hard_skill = models.ForeignKey(HardSkill, verbose_name='Хард скилл', related_name='hard_skill')

    def __str__(self):
        return self.soft_skill, self.hard_skill


class Profession(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    slug = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

    def __str__(self):
        return self.title

class Goal(models.Model):
    profession = models.ForeignKey(Profession, verbose_name='Профессия', related_name='profession')
    level = models.ForeignKey(Level, verbose_name='Уровень', related_name='level')
    garde = models.IntegerField()

    def __str__(self):
        return self.profession, self.level