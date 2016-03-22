from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models 

class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(blank=True)
	rating = models.IntegerField(blank=True)
	author = models.CharField(max_length=30)
	likes = models.ManyToManyField(User)

	def __str__(self):
		return '%s : %s : %s' % (self.author, self.title, self.text)

	def get_url(self):
		return '/question/%d' % self.pk

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField()
	question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
	author = models.CharField(max_length=30)

	def __str__(self):
		return '%s : Re:%s : %s' % (self.author, self.question, self.text)
