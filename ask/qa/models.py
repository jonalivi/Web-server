from __future__ import unicode_literals

from django.core.urlresolvers import reverse
#from django.contrib.auth.models import User
from django.db import models 

from django.utils import timezone

class User(models.Model):
	username = models.CharField(max_length=20, unique=True)
	email = models.EmailField()
	password = models.CharField(max_length=20)

	def __str__(self):
		return '%s, %s' % (self.username, self.email)

class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(default=timezone.now())
	rating = models.IntegerField(default=0)
	author = models.CharField(max_length=30, default='anon')
	likes = models.ManyToManyField(User)

	def __str__(self):
		return '%s : %s : %s' % (self.author, self.title, self.text)

	def get_url(self):
		return '/question/%d/' % self.pk

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(default=timezone.now())
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	author = models.CharField(max_length=30, default='anon')

	def __str__(self):
		return '%s : Re:%s : %s' % (self.author, self.question, self.text)



