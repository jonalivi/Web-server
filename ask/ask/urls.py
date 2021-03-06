"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.questions_main, name='questions-main'),
	url(r'^login/', views.login, name='login'),
	url(r'^signup/', views.signup, name='signup'),
	url(r'^question/(?P<question_id>\d+)/$', views.question_single, name='question-single'),
	url(r'^ask/', views.question_add, name='question-add'),
	url(r'^answer/', views.answer_add, name='answer-add'),
	url(r'^popular/', views.questions_popular, name='questions-popular'),
	url(r'^new/', views.test),
]
