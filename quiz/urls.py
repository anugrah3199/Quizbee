from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^result', views.result, name = 'result'),
    url(r'^created', views.created, name = 'created'),
    url(r'^about', views.about, name = 'about'),
    url(r'^add_question',views.add_question,name = 'add_question'),
    url(r'^(?P<choice>[\w]+)', views.questions, name = 'questions'),
]
