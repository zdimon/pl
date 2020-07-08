from django.shortcuts import render
from django.http import HttpResponse

def index(r):
    return render(r,'index.html',{'var': 'value'})

def about(request):
    return render(request,'about.html')
