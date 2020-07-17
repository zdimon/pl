from django.shortcuts import render
from django.http import HttpResponse
from course.models import Course, Lesson

from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

from pl.settings import DATA_DIR
from course.models import parse_md

def index(request):
    courses = Course.objects.all()
    return render(request,'index.html',{'courses': courses})



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
