from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models 

class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField()
	rating = models.IntegerField()
	author = User()
	likes = models.ManyToManyField(User)

	def __str__(self):
		return '%s : %s : %s' % (self.author, self.title, self.text)

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField()
	question = models.OneToOneField(Question)
	author = User()

	def __str__(self):
		return '%s : Re:%s : %s' % (self.author, self.question, self.text)
