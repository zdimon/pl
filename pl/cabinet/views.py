from django.shortcuts import render
from course.models import LessonPayments
from django.contrib import messages
from django.shortcuts import redirect

def index(request):
    return render(request,'cabinet_index.html')

from .forms import ProfileForm

def edit_profile(request):
    user = request.user.userprofile
    
    if request.method == 'POST':
        form = ProfileForm(data = request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.info(request, 'Спасибо. Ваш профиль был сохранен.')
            return redirect('cabinet_index')
    else:
        form = ProfileForm(instance=user)
    return render(request,'edit_profile.html', {'form': form})

def payments(request):
    payments = LessonPayments.objects.filter(user=request.user).order_by('-id')
    return render(request,'payments.html',{'payments': payments})

