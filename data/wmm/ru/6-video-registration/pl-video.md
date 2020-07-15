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
