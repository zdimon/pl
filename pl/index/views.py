from django.shortcuts import render
from django.http import HttpResponse
from course.models import Course, Lesson, Topic

from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

from pl.settings import DATA_DIR, SB_DOMAIN
from course.models import parse_md
from tagging.models import Tag

def index(request):
    courses = Course.objects.filter(is_active=True).order_by('-order')
    last_lessons = Lesson.objects.all().order_by('-id')[0:5]
    tags = Tag.objects.all().order_by('name')
    last_topics = Topic.objects.all().order_by('-id')[0:6]
    last_topics2 = Topic.objects.all().order_by('-id')[6:12]

    return render(request,'index.html', \
    {'courses': courses, \
    'last_lessons': last_lessons, \
    'tags': tags, \
    'last_topics': last_topics, \
	'last_topics2': last_topics2, \
    'last_lessons': last_lessons, \
    'sb_domain': SB_DOMAIN \
    })



def about(request):
    
    return render(request,'about.html')

def oferta(request):
    path = DATA_DIR+'/oferta.md'
    f = open(path, 'r')
    txt = f.read()
    f.close()
    oferta = parse_md(txt)    
    return render(request,'md.html', {'text': oferta})

def delivery(request):
    path = DATA_DIR+'/delivery.md'
    f = open(path, 'r')
    txt = f.read()
    f.close()
    oferta = parse_md(txt)    
    return render(request,'md.html', {'text': oferta})   

def confident(request):
    path = DATA_DIR+'/confident.md'
    f = open(path, 'r')
    txt = f.read()
    f.close()
    oferta = parse_md(txt)    
    return render(request,'md.html', {'text': oferta})   



class LoginView(View):

    def get(self, request):
        return render(request,'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')

        return render(request, "index.html")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
