from django.shortcuts import render
from django.http import HttpResponse
from course.models import Course, Lesson

def index(request):
    courses = Course.objects.all()
    return render(request,'index.html',{'courses': courses})

def course_detail(request,slug):
    course = Course.objects.get(name_slug=slug)
    return render(request,'course_detail.html',{'course': course})

def lesson_detail(request,slug):
    lesson = Lesson.objects.get(name_slug=slug)
    return render(request,'lesson_detail.html',{'lesson': lesson})

def about(request):
    
    return render(request,'about.html')
