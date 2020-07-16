# Оплата уроков.

Заполняем номер уроков в классе CourseLoader.

    def save_lessons(self):
        ...
        for d in onlydirs:
            ...
            number = d.split('-')[0]
            lesson.number = number 

Делаем сортировку во вью.

    def course_detail(request,slug):
        course = Course.objects.get(name_slug=slug)
        lessons = Lesson.objects.filter(course=course).order_by('number')
        return render(request,'course_detail.html',{'course': course, 'lessons': lessons})

Выводим в шаблоне.

    {% for lesson in lessons %}
            <li>{{ lesson.number }}. <a href="{{ lesson.get_absolute_url }}">{{ lesson.title }}</a></li>
    {% endfor %}

Отображаем первый урок бесплатно, остальные запрещаем.

    def lesson_detail(request,slug):
        is_free = False
        lesson = Lesson.objects.get(name_slug=slug)
        if lesson.number == 1:
            is_free = True
        return render(request,'lesson_detail.html',{'lesson': lesson, 'is_free': is_free})

Шаблон.

    {% if is_free %}
    <div class="full">
        <div class="heading_main text_align_left">
            <h2>{{ lesson.title }}</h2>

        </div>
        <div class="text_align_right">
            <a href="{{ lesson.course.get_absolute_url }}">Назад</a>
            </div>
        {% for topic in lesson.topic_set.all %}
            <div class="full"> 
                
                {{topic.video_tag}}

                {{ topic.content }}

            </div>   
        {% endfor %} 
    
    </div>
    {% else %}
        <div class="alert alert-danger" role="alert">
            Для просмотра урока его необходимо оплатить.
        </div>
    {% endif %}

Создадим новую вьюху для страницы оплаты.

    from pl.settings import LESSON_PRICE

    def pay(request,lesson_id):
        lesson = Lesson.objects.get(pk=lesson_id)
        return render(request,'pay.html',{'lesson': lesson, 'price': LESSON_PRICE})


Шаблон.

    {% extends 'layout.html' %}
    {% block carousel %} {% endblock %}
    {% block content %}

    <div class="section margin-top_50">
        <div class="container">
            <div class="row">
                <div class="col-md-12 layout_padding_2">
                    <div class="full">
                        <div class="heading_main text_align_left">
                        <h2>Покупка урока</h2>

                        </div>
                        <div class="full">
                            <p class="big-text">Курс: 
                                <a href="{{ lesson.course.get_absolute_url }}">
                                    {{ lesson.course }}
                                </a>
                            </p>
                            <p class="big-text">Урок: 
                                <a href="{{ lesson.get_absolute_url }}">
                                    {{ lesson }}
                                </a>
                            </p>
                            <p class="big-text">Стоимость: 
                            {{ price }} грн.
                            </p>
                        </div>
                        <div class="full center">
                            <a class="contact_bt" href="">Оплатить {{ price }} грн.</a>
                        </div>

                    </div>
                </div>
            </div>        
        </div>
    </div>

{% endblock %}


Роутинг.

    from django.urls import path, include
    from .views import course_detail, lesson_detail, pay

    urlpatterns = [ 
        path('detail/<slug:slug>',course_detail, name="course_detail"),
        path('lesson/detail/<slug:slug>',lesson_detail, name="lesson_detail"),
        path('pay/<int:lesson_id>',pay, name="pay"),
    ]

Устанавливаем библиотку ликпея.

    git+https://github.com/liqpay/sdk-python#egg=liqpay

Берем секреты ликпей, устанавливаем урл для приема платежей и стоимость.

[ссылка для входа](https://www.liqpay.ua/)

    LIQPAY_PUBLIC_KEY   = 'i33...'
    LIQPAY_PRIVATE_KEY  = 'SsTKt...'
    LIQPAY_PROCESS_URL  = 'https://learning.webmonstr.com/liqpay/process'
    LESSON_PRICE = 50

Создаем модель для платежей и миграции.

    # PAYMENT MODEL

    from django.contrib.auth.models import User

    class LessonPayments(models.Model):
        user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null = True)
        lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, blank=True, null = True)
        is_paid = models.BooleanField(default=False)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)   
      
    ################################ 

Админка.

 

Создаем новый платеж во вьюхе и передаем кнопку в шаблон.


    from django.urls import reverse
    ...
    @login_required
    def pay(request,lesson_id):
        
        lesson = Lesson.objects.get(pk=lesson_id)
        liqpay = LiqPay(LIQPAY_PUBLIC_KEY, LIQPAY_PRIVATE_KEY)
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

Выводим в шаблоне.

    <a>{{ button | safe }}</a>

Делаем вьюху для приема платежей.

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
    
Добавляем в роутинг.

    from course.views import liqpay_process

    urlpatterns = [
        ...
        path('liqpay/process/', liqpay_process),
    ]

Добавим метод в модель для проверки оплаченного урока.

    class Lesson(models.Model):
        ...
        
        def is_paid(self,user):
            if self.number == 1:
                return True
            try:
                LessonPayments.objects.get(user=user,lesson=self, is_paid=True)
                return True
            except:
                return False

Перепишем вьюху.


    @login_required
    def lesson_detail(request,slug):
        lesson = Lesson.objects.get(name_slug=slug)
        is_free = lesson.is_paid(request.user)
        return render(request,'lesson_detail.html',{'lesson': lesson, 'is_free': is_free})

![admin]({path-to-subject}/images/1.png)

