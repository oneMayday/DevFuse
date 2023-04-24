from django.contrib.auth.models import User
from django.db import models


class Technologie(models.Model):
	title = models.CharField('Название технологии', max_length=50, unique=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Технология'
		verbose_name_plural = 'Технологии'

	def __str__(self):
		return self.title

	def __repr__(self):
		return self.title


class Specialization(models.Model):
	title = models.CharField('Название специализации', max_length=50)

	class Meta:
		verbose_name = 'Специализация'
		verbose_name_plural = 'Специализации'

	def __repr__(self):
		return self.title

	def __str__(self):
		return self.title


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
	name = models.CharField(max_length=50, blank=True, null=True)
	surname = models.CharField(max_length=50, blank=True, null=True)
	city = models.CharField(max_length=50, blank=True, null=True)
	about = models.TextField(max_length=500, blank=True, null=True)
	specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, blank=True, null=True)
	skills = models.ManyToManyField(Technologie, blank=True)
	telegram = models.URLField(blank=True, null=True)
	github = models.URLField(blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Профиль'
		verbose_name_plural = 'Профили'

	def __str__(self):
		return f'Профиль {self.user.username}'

	def __repr__(self):
		return f'Профиль {self.user.username}'