from django.contrib.auth.models import User
from django.db import models


class Skill(models.Model):
	title = models.CharField(max_length=50, unique=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Технология'
		verbose_name_plural = 'Технологии'

	def __str__(self):
		return self.title

	def __repr__(self):
		return self.title


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
	nickname = models.CharField(max_length=50, unique=True, blank=True, null=True)
	name = models.CharField(max_length=50, blank=True, null=True)
	surname = models.CharField(max_length=50, blank=True, null=True)
	email = models.EmailField(max_length=50, blank=True, unique=True, null=True)
	city = models.CharField(max_length=50, blank=True, null=True)
	about = models.TextField(max_length=500, blank=True, null=True)
	skills = models.ManyToManyField(Skill, blank=True)
	telegram = models.URLField(max_length=100, blank=True, null=True)
	github = models.URLField(max_length=100, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Профиль'
		verbose_name_plural = 'Профили'
