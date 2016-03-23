from django.http import HttpRequest, HttpResponse, Http404
from django.core.paginator import Paginator, Page, EmptyPage
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponseRedirect

from qa.models import Question, Answer, User
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm

def test(request, *args, **kwargs):
	return HttpResponse('OK')

@require_GET
def questions_main(request):
	questions = Question.objects.all()
	questions = questions.order_by('-added_at', '-id')
	try:
		page = int(request.GET.get('page', 1))
	except ValueError:
		raise Http404
	paginator = Paginator(questions, 10)
	paginator.baseurl = '/?page='
	try:
		page = paginator.page(page)
	except EmptyPage:
		raise Http404
	return render(request, 'questions_all.html', {
		'questions':	page.object_list,
		'paginator':	paginator,
		'page':		page,
	})

@require_GET
def questions_popular(request):
	questions = Question.objects.all()
	questions = questions.order_by('-rating', '-added_at', '-id')
	try:
		page = int(request.GET.get('page', 1))
	except ValueError:
		raise Http404
	paginator = Paginator(questions, 10)
	paginator.baseurl = '/popular/?page='
	try:
		page = paginator.page(page)
	except EmptyPage:
		raise Http404
	return render(request, 'questions_popular.html', {
		'questions':	page.object_list,
		'paginator':	paginator,
		'page':		page,
	})
	
	
@ensure_csrf_cookie
def question_single(request, question_id=None):
	if not question_id:
		raise Http404
	question_id = int(question_id)
	q = Question.objects.filter(pk=question_id)
	if not q:
		raise Http404
	try:
		q = q[0]
	except IndexError:
		raise Http404
	answers = Answer.objects.filter(question=q).order_by('-added_at')
	return render(request, 'question.html', {
		'question':	q,
		'answers':	answers,
	})

def question_add(request):
	if request.method == 'POST':
		form = AskForm(request.POST)
		if form.is_valid():
			question = form.save()
			question.author_id = int(request.session.get('user'))
			question.save()
			url = question.get_url()
			return HttpResponseRedirect(url)
	else:
		user_id = request.session.get('user')
		if not user_id:
			return HttpResponseRedirect('/login/')
		form = AskForm()
	return render(request, 'question_add.html', {
		'form':	form,
	})

def answer_add(request):
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		if form.is_valid():
			answer = form.save()
			answer.author_id = int(request.session.get('user'))
			answer.save()
			url = answer.question.get_url()
			return HttpResponseRedirect(url)
	else:
		user_id = request.session.get('user')
		if not user_id:
			return HttpResponseRedirect('/login/')
		form = AnswerForm()
	return render(request, 'answer_add.html', {
		'form':	form,
	})	

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			request.session.flush()
			request.session['user'] = user.id
			return HttpResponseRedirect('/')
	else:
		form = SignupForm()
	return render(request, 'signup_form.html', {
		'form': form,
	})

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = form.save()
			request.session.flush()
			request.session['user'] = user.id
			return HttpResponseRedirect('/')
	else:
		form = LoginForm()
	return render(request, 'login_form.html', {
		'form': form,
	})	


