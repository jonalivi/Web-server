from django import forms
from qa.models import Question, Answer, User

from django.utils import timezone

class AskForm(forms.Form):
	title = forms.CharField(max_length=255)
	text = forms.CharField(widget=forms.Textarea)

	def clean(self):
		self.cleaned_data['added_at'] = timezone.now()
		return self.cleaned_data
		
	def save(self):
		q = Question(**self.cleaned_data)
		q.save()
		return q

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.ModelChoiceField(queryset = Question.objects.all(), to_field_name='title')

	def clean(self):
		self.cleaned_data['added_at'] = timezone.now()
		return self.cleaned_data
		
	def save(self):
		a = Answer(**self.cleaned_data)
		a.save()
		return a

class SignupForm(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username='username')
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Username already in use', code='wrong')

	def save(self):
		user = User(**self.cleaned_data)
		user.save()
		return user

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
