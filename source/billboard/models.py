from django.contrib.auth.models import User
from django.db import models

from users.models import Technologie


class Publication(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', max_length=4000)
    technology_stack = models.ManyToManyField(Technologie, verbose_name='Cтек технологий', )
    team = models.ManyToManyField(User, verbose_name='Команда')

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title
