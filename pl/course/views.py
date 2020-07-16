from django.shortcuts import render
from django.http import HttpResponse
from course.models import Course, Lesson

from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from pl.settings import LESSON_PRICE
from django.contrib.auth.decorators import login_required

from liqpay.liqpay3 import LiqPay
from pl.settings import LIQPAY_PRIVATE_KEY, LIQPAY_PUBLIC_KEY, LIQPAY_PROCESS_URL, DOMAIN, LESSON_PRICE
import time
from .models import LessonPayments
from django.urls import reverse

@login_required
def pay(request,lesson_id):
    
    lesson = Lesson.objects.get(pk=lesson_id)
    liqpay = LiqPay(LIQPAY_PUBLIC_KEY, LIQPAY_PRIVATE_KEY)
    try:
        lp = LessonPayments.objects.get(user=request.user,lesson=lesson)
    except:
        lp = LessonPayments.objects.create(
            user = request.user, \
            lesson = lesson
        )
    form_html = liqpay.cnb_form({
        'action': 'pay',
        'amount': LESSON_PRICE,
        'currency': 'UAH',
        'description': 'Payment for the lesson',
        'order_id': lp.pk,
        'version': '3',
        'sandbox': 1,
        'result_url': DOMAIN+reverse('lesson_detail', args=(lesson.name_slug,))
    })
    return render(request,'pay.html',{'lesson': lesson, 'price': LESSON_PRICE, 'button': form_html})

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def liqpay_process(request):
    print(request.POST)
    liqpay = LiqPay(LIQPAY_PUBLIC_KEY, LIQPAY_PRIVATE_KEY)
    data = request.POST.get('data')
    signature = request.POST.get('signature')
    sign = liqpay.str_to_sign(LIQPAY_PRIVATE_KEY + data + LIQPAY_PRIVATE_KEY)
    if sign == signature:
        print('callback is valid')
        data = liqpay.decode_data_from_str(data)
        order = LessonPayments.objects.get(pk=data['order_id'])
        order.is_paid = True
        order.save()
    return HttpResponse('ok')

def course_detail(request,slug):
    course = Course.objects.get(name_slug=slug)
    lessons = Lesson.objects.filter(course=course).order_by('number')
    paid = []
    for l in lessons:
        if l.is_paid(request.user):
            paid.append(l.id)
    print(paid)
    return render(request,'course_detail.html',{'course': course, 'lessons': lessons, 'paid': paid, 'price': LESSON_PRICE})

@login_required
def lesson_detail(request,slug):
    lesson = Lesson.objects.get(name_slug=slug)
    is_free = lesson.is_paid(request.user)
    return render(request,'lesson_detail.html',{'lesson': lesson, 'is_free': is_free})


@login_required
def my_cabinet(request):
    payments = LessonPayments.objects.filter(user=request.user).order_by('-id')
    return render(request,'my_cabinet.html',{'payments': payments})
