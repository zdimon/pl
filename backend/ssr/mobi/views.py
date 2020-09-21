from django.shortcuts import render

def mobi_index(request,slug=None):
    return render(request,'mobi/index.html')