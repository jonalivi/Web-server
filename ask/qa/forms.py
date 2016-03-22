from django import forms
from qa.models import Question, Answer

from django.utils import timezone

class AskForm(forms.Form):
	title = forms.CharField(max_length=255)
	text = forms.CharField(widget=forms.Textarea)

	def clean(self):
		self.cleaned_data['added_at'] = timezone.now()
		
	def save(self):
		q = Question(**self.cleaned_data)
		q.save()
		return q

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.ModelChoiceField(queryset = Question.objects.all(), to_field_name='title')

	def clean(self):
		self.cleaned_data['added_at'] = timezone.now()
		
	def save(self):
		a = Answer(**self.cleaned_data)
		a.save()
		return a
