from django.shortcuts import render
from course.models import LessonPayments
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

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

from cabinet.models import Promocode
from django.views.generic import ListView
from course.models import Course

class PromocodeList(ListView):
    model = Promocode
    def get_context_data(self, *args, **kwargs):
        context = super(PromocodeList, self).get_context_data(*args, **kwargs)
        context['courses'] = Course.objects.all()
        return context

import os
import base64

def secure_rand(len=8):
    token=os.urandom(len)
    return base64.b64encode(token).decode("utf-8").replace('=','')

def promo_gen(request):
    if request.method == 'POST':
        messages.info(request, 'Промокоды сгенерированы.')
        course = Course.objects.get(pk = request.POST.get('course'))
        for i in range(0,int(request.POST.get('ammount'))):
            try:
                p = Promocode()
                p.code = secure_rand()
                p.course = course
                p.save()
            except:
                pass
        return redirect('promo')

@login_required
def promo_activate(request,slug):
    code = Promocode.objects.get(code=slug)
    if code.is_activated:
        messages.info(request, 'Этот промокод уже активирован!')
    else:
        code.activate(request.user.userprofile)
        messages.info(request, 'Промокод активирован.')
    return redirect('promo')