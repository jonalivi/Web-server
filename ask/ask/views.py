from django.http import HttpRequest, HttpResponse, Http404
from django.core.paginator import Paginator, Page, EmptyPage
from django.shortcuts import render
from django.views.decorators.http import require_GET
from qa.models import Question, Answer

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
	
	
@require_GET
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
