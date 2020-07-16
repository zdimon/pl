# Импорт видео.
    
Определим константу с путем к видео файлам.

    VIDEO_DIR = '/home/zdimon/Videos/course-data/ruslan'

Добавим поле с видео в модель.

    class Topic(models.Model):
        ...
        video = models.CharField(verbose_name='Name slug',max_length=250, blank=True)
        has_video = models.BooleanField(default=False)

Создадим и применим миграцию.

        ./manage.py makemigrations
        ./manage.py migrate

Админка.

    @admin.register(Topic)
    class TopicAdmin(admin.ModelAdmin):
        list_display = [... 'video', 'has_video']

Доработаем класс модели.


    class Topic(models.Model):
        ...

        def check_video(self):
            onlyfiles = [f for f in listdir(VIDEO_DIR) if isfile(join(VIDEO_DIR, f))]
            for video in onlyfiles:
                fname = video.split('.')[0]
                if fname == self.filename.split('.')[0]:
                    self.has_video = True
                    self.video = video
                    self.save()

Вызовем метод в загрузчике.

    class CourseLoader(object):

    ...

        def save_lessons(self):
            ...
                for f in data['files']:
                    ...
                    topic.check_video()

![admin]({path-to-subject}/images/1.png)

![admin]({path-to-subject}/images/2.png)

## Выведем видео на страницу.

Создадим симлинк на каталог с виде в папке static.

    ln -s /home/zdimon/Videos/course-data/ruslan/ video


Создадим метод в модели.

    @property
    def video_tag(self):
        if self.has_video:
            return mark_safe('<video  controls><source src="/static/video/%s" type="video/mp4"></video>' % self.video)
        else:
            return 'Видео отсутствует'

Выведем в шаблоне.

    {{topic.video_tag}}

## Ссылка назад.

    <div class="text_align_right">
        <a href="{{ lesson.course.get_absolute_url }}">Назад</a>
    </div>

## Регистрация.

    pip install social-auth-app-django

Добавляем в настройки.

    INSTALLED_APPS = [
    ...
        'social_django'
    ]

Применяем миграцию.

![admin]({path-to-subject}/images/3.png)

Добавляем секреты и бекенд.

    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '...'
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '...'
    SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

    AUTHENTICATION_BACKENDS = (
        'social_core.backends.open_id.OpenIdAuth',
        'social_core.backends.google.GoogleOpenId',
        'social_core.backends.google.GoogleOAuth2',
        'social_core.backends.google.GoogleOAuth',
        'django.contrib.auth.backends.ModelBackend',
    )

Добавляем роутинг.

        urlpatterns = [
        ...
        path('social-auth/', include('social_django.urls', namespace="social")),
    ]

[Получаем секреты](https://console.developers.google.com/.)

![admin]({path-to-subject}/images/5.png)

Определяем вьюхи для авторизации и выхода.

    from django.views.generic import View
    from django.contrib.auth import authenticate, login, logout
    from django.http import HttpResponse, HttpResponseRedirect
    ...
    class LoginView(View):
        def post(self, request):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/')

            return render(request, "index.html")

    class LogoutView(View):
        def get(self, request):
            logout(request)
            return HttpResponseRedirect('/')

Прописываем роутинг.

    from index.views import LoginView, LogoutView

    urlpatterns = [
        ...
        path('logout/', LogoutView.as_view(), name='logout'),
        path('login/', LoginView.as_view(), name='login'),
    ]

Выводим ссылки в шаблоне.

    {% if user.is_authenticated %}
    <li><a class="nav-link" href="news.html">Мой кабинет</a></li>
    <li>
        <a class="nav-link" id="logout" href="{% url 'logout' %}" class="">Выход</a>
    </li>
    {% else %}
    <li>
        <a class="nav-link" href='{% url "social:begin" "google-oauth2" %}'>
            Вход <img height="30" src="/static/images/google.png" />
        </a>
    </li>
    {% endif %}

![admin]({path-to-subject}/images/6.png)