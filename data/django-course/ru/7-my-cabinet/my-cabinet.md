# Кабинет пользователя.
    
Создаем вьюху под кабинет.

    @login_required
    def my_cabinet(request):
        payments = LessonPayments.objects.filter(user=request.user).order_by('-id')
        return render(request,'my_cabinet.html',{'payments': payments})

Добавляем в роутинг.

    from django.urls import path, include
    from .views import ... my_cabinet

    urlpatterns = [ course_detail, lesson_detail, pay, 
        ...
        path('my/cabinet',my_cabinet, name="my_cabinet"),
    ]

Выводим в шаблоне.

    {% extends 'layout.html' %}
    {% block carousel %} {% endblock %}
    {% block content %}

    <div class="section margin-top_50">
        <div class="container"> 
            <div class="row">
                <div class="col-md-12 layout_padding_2">
                    <h1>Мой кабинет</h1>
                    {% if payments %}
                    <table class="table">
                        <thead>
                        <tr>
                            <th scope="col">#</th>
                            <th scope="col">Название урока</th>
                            <th scope="col">Курс</th>
                            <th scope="col">Цена</th>
                            <th scope="col">Дата покупки</th>
                        </tr>
                        </thead>
                        <tbody>
                        
                            {% for payment in payments %}
                            <tr>
                                <th scope="row">{{ payment.id }}</th>
                                <td>{{ payment.lesson }}</td>
                                <td>{{ payment.lesson.course }}</td>
                                <td>50 грн</td>
                                <td>{{ payment.created }} </td>
                            </tr>
                            {% endfor %}
                        
                        </tbody>
                    </table>
                    {% else %}
                        <div class="alert alert-danger" role="alert">
                            У вас нет купленных уроков.
                        </div>
                    {% endif %}

                </div>
            </div>        
        </div>
    </div>

    {% endblock %}