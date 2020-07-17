# Вопросы, комментарии.
      
Создадим модель для вопросов.

При этом воспользуемся библиотекой mptt.

[ссылка на документацию](https://django-mptt.readthedocs.io/en/latest/index.html)

Устанавливаем.

    pip install django-mptt

Прописываем в настройках.

    INSTALLED_APPS = [
    ...
        'mptt'
    ]

Создаем модель.

    from mptt.models import MPTTModel, TreeForeignKey

    class Comments(MPTTModel):
        content = models.TextField()
        user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null = True)
        parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
        created = models.DateTimeField(auto_now_add=True)
        lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, blank=True, null = True)
        is_published = models.BooleanField(default=False)        
        class MPTTMeta:
            order_insertion_by = ['user']

Проводим миграцию.

Выводим форму под уроком.


    <div class="section contact_section" style="background:#12385b;">
        <div class="container">
            <div class="row">
                
                <div class="layout_padding col-lg-12 col-md-12 col-sm-12">
                    <div class="contact_form">
                        <span class="white-title">Задать вопрос, прокомментировать.</span>
                        <form action="{% url 'save_comment' %}" method="POST"
                        {% csrf_token %}
                        <input name="lesson_id" value="{{ lesson.id }}" />
                        <fieldset>
                            
                            <div class="full field">
                                <textarea placeholder="Massage" name="message"></textarea>
                            </div>
                            <div class="full field">
                                <div class="center"><button>Отправить</button></div>
                            </div>
                        </fieldset>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>




## Фреймворк сообщений.

[ссылка на документацию](https://docs.djangoproject.com/en/3.0/ref/contrib/messages/)

Выводим сообщение в layout.html

    {% if messages %}
        {% for message in messages %}
            <div class="section" style="margin-top: 100px;">
                <div class="container">
                    <div class="full">
                        <div class="alert alert-success" role="alert">
                            {{ message }}
                        </div>
                    </div>
                </div>
            </div>
        {% endfor %}
    {% endif %}

Функция-вьюха.


    from django.shortcuts import redirect
    from django.contrib import messages

    @login_required
    def save_comment(request):
        if request.method == 'POST':
            lesson = Lesson.objects.get(pk=request.POST.get('lesson_id'))
            comment = Comments()
            comment.lesson = lessonname="message"
            comment.user = request.user
            comment.content = request.POST.get('message')
            comment.save()
            messages.info(request, 'Спасибо. Ваш комментарий был сохранен.')
            return redirect(lesson)

## Раздел обсуждений.

Вьюха.

    @login_required
    def discussion(request):
        comments = Comments.objects.filter(is_published=True).order_by('-id')
        return render(request,'discussion.html',{'comments': comments})

Роут.

    urlpatterns = [ 
        ...
        path('discussion',discussion, name="discussion"),
    ]

Шаблон discussion.html.

    {% extends 'layout.html' %}
    {% block carousel %} {% endblock %}
    {% block content %}

    <div class="section margin-top_50">
        <div class="container"> 
            <div class="row">
                <div class="col-md-12 layout_padding_2">
                    <h1>Обсуждение</h1>
                    
                    <table class="table">
                        <thead>
                          <tr>
                            <th scope="col">#</th>
                            <th scope="col">Сообщение</th>
                            <th scope="col">Название урока</th>
                            
                            <th scope="col">Автор</th>
                            <th scope="col">Ответов</th>
                            <th scope="col">Дата</th>
                          </tr>
                        </thead>
                        <tbody>
                         
                            {% for message in comments %}
                            <tr>
                                <th scope="row">{{ message.id }}</th>
                                <td>{{ message.content }}</td>
                                <td>{{ message.lesson }}</td>
                                <td>{{ message.user }}</td>
                                <td>0</td>
                                <td>{{ message.created }} </td>
                            </tr>
                            {% endfor %}
                          
                        </tbody>
                      </table>
                     

                </div>
            </div>        
        </div>
    </div>

    {% endblock %}

![admin]({path-to-subject}/images/2.png)

## Постраничная навигация.



