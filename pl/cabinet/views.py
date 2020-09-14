from django.shortcuts import render
from course.models import LessonPayments, Comments, Lesson
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from cabinet.forms.forms import MyCommentForm
from django.urls import reverse
from liqpay.liqpay3 import LiqPay
from cabinet.models import ReplCredit

from pl.settings import LIQPAY_PRIVATE_KEY, LIQPAY_PUBLIC_KEY, LIQPAY_PROCESS_URL, DOMAIN


def index(request):
    courses = Course.objects.all().order_by('-id')
    return render(request,'main.html', {'courses': courses})


def show_lesson(request,id):
    lesson = Lesson.objects.get(pk=id)
    return render(request,'show_lesson.html', {'lesson': lesson})


def add_credits(request):

    return render(request,'add_credits.html')

@csrf_exempt
def pay_success(request):

    return render(request,'pay_success.html')

def get_liqpay_form(request, credit):
    r = ReplCredit()
    r.user = request.user.userprofile
    r.ammount = credit
    r.save()
    liqpay = LiqPay(LIQPAY_PUBLIC_KEY, LIQPAY_PRIVATE_KEY)
    form_html = liqpay.cnb_form({
        'action': 'pay',
        'amount': credit,
        'currency': 'UAH',
        'description': 'Payment for the lesson',
        'order_id': '%s-%s' % (request.user.id,r.id),
        'version': '3',
        'result_url': DOMAIN+reverse('pay_success')
    })
    return render(request,'liqpay_form.html', {'form_html': form_html})





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

class PromocodeList(LoginRequiredMixin,ListView):
    model = Promocode
    def get_context_data(self, *args, **kwargs):
        if self.request.user.is_superuser:
            context = super(PromocodeList, self).get_context_data(*args, **kwargs)
            context['courses'] = Course.objects.all()
            return context
        else:
            redirect('access_denite')

import os
import base64

def secure_rand(len=8):
    token=os.urandom(len)
    return base64.b64encode(token).decode("utf-8").replace('=','').replace('/','').replace('+','')

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

def access_denite(request):
    return render(request,'access_denite.html')

def faq(request):
    comments = Comments.objects.filter(is_published=True, level=0).order_by('-id')
    return render(request,'faq.html',{'comments': comments})

from cabinet.forms import CommentForm

def add_answer(request,id):
    comment = Comments.objects.get(pk=id)
    answer = Comments()
    answer.user = request.user.userprofile
    answer.parent = comment
    answer.lesson = comment.lesson
    answer.is_published = True
    form = CommentForm(request.POST or None, instance=answer)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.info(request, 'Спасибо. Ваш комментарий был сохранен.')
            return redirect('faq')
    return render(request,'add_answer.html',{'form': form, 'comment': comment})