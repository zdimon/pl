from django.shortcuts import render

def mobi_index(request):
    return render(request,'mobi/index.html')