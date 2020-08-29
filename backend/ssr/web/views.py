from django.shortcuts import render

def web_index(request):
    return render(request,'web/index.html')