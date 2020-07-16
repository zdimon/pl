# Импорт уроков и тем.

Добавляем два новых класса в модель.

    class Lesson(models.Model):
        title = models.CharField(max_length=250, blank=True, verbose_name=_(u'Name'))
        number = models.IntegerField(default=0, verbose_name=_(u'Number'))
        is_active = models.BooleanField(verbose_name=_('Is main?'), default=False)
        image = models.ImageField(blank=True, verbose_name=_(u'Image'), upload_to='lessons_images', null = True)
        course = models.ForeignKey(Course, verbose_name=_(u'Course'), on_delete=models.CASCADE)
        name_slug = models.CharField(verbose_name='Name slug',max_length=250, blank=True)

    class Topic(models.Model):
        title = models.CharField(max_length=250, blank=True, verbose_name=_(u'Name'))
        filename = models.CharField(verbose_name='Name slug',max_length=250, blank=True)
        lesson = models.ForeignKey(Lesson, verbose_name=_(u'Lesson'), on_delete=models.CASCADE)

Создаем и применяем миграцию.

![admin]({path-to-subject}/images/1.png)

Админ интерфейс.

    from django.contrib import admin

    from course.models import Course, Lesson, Topic

    @admin.register(Course)
    class CourseAdmin(admin.ModelAdmin):
        list_display = ['image_tag', 'name_slug', 'desc', 'name', 'meta_title']


    @admin.register(Lesson)
    class LessonAdmin(admin.ModelAdmin):
        list_display = ['title', 'name_slug', 'course']

    @admin.register(Topic)
    class TopicAdmin(admin.ModelAdmin):
        list_display = ['title', 'filename', 'lesson']

Добавляем новый метод save_lessons в класс CourseLoader

class CourseLoader(object):
    ...

    def save_lessons(self):
        path = DATA_DIR+'/'+self.dir+'/ru'
        onlydirs = [f for f in listdir(path) if isdir(join(path, f))]
        for d in onlydirs:
            lesson_yml_path = path+'/'+d+'/meta.yml'
            data = self.get_meta(lesson_yml_path)
            print(data)
            try:
                lesson = Lesson.objects.get(name_slug=d)
            except:
                lesson = Lesson()
            lesson.name_slug = d
            lesson.title = data['name']
            lesson.course = self.course
            lesson.save()
            print('Saving lesson...%s' % data['slug'])
            for f in data['files']:
                try:
                    topic = Topic.object.get(lesson=lesson,filename=f['file'])
                except:
                    topic = Topic.objects.create(filename=f['file'], title=f['title'], lesson=lesson)
                print('Saving topic %s' % f['file'])

Выводим курсы на главную страницу.

    from course.models import Course

    def index(request):
        courses = Course.objects.all()
        return render(request,'index.html',{'courses': courses})

Шаблон.

    {% extends 'layout.html' %}
    {% block carousel %} {% endblock %}
    {% block content %}

    <div class="section margin-top_50">
        <div class="container">
            {% for course in courses %}
            <div class="row">
                <div class="col-md-6 layout_padding_2">
                    <div class="full">
                        <div class="heading_main text_align_left">
                           <h2>{{ course.name }}</h2>
                        </div>
                        <div class="full">
                          <p>{{ course.desc }}</p>
                        </div>
                        <div class="full">
                           <a class="hvr-radial-out button-theme" href="#">Подробней</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="full">
                        <img src="{{ course.image.url }}" alt="#" />
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>

    {% endblock %}

## Страница содержимого курса.


### URL роутинг.

    from index.views import .., course_detail

    urlpatterns = [
        ...
        path('course/detail/<slug:slug>',course_detail, name="course_detail"),
       .
    ]

### Модель course/models.py.

    from django.urls import reverse

    class Course(models.Model):
        ...

        def get_absolute_url(self):
            return reverse('course_detail', kwargs={'slug': self.name_slug })

### Вьюха index/views.py.

    def course_detail(request,slug):
        course = Course.objects.get(name_slug=slug)
        return render(request,'course_detail.html',{'course': course})


### Шаблон templates/course_detail.html.

    {% extends 'layout.html' %}
    {% block carousel %} {% endblock %}
    {% block content %}

    <div class="section margin-top_50">
        <div class="container">
            <div class="row">
                <div class="col-md-12 layout_padding_2">
                    <div class="full">
                        <div class="heading_main text_align_left">
                           <h2>{{ course.name }}</h2>
                        </div>
                        <div class="full">
                            <ul class="lessons-list">
                                {% for lesson in course.lesson_set.all %}
                                     <li><a href="#">{{ lesson.title }}</a></li>
                                {% endfor %}
                             </ul>
                        </div>
                    </div>
                </div>
            </div>        
        </div>
    </div>

    {% endblock %}


![admin]({path-to-subject}/images/2.png)

![admin]({path-to-subject}/images/3.png)

Создадим симлинк в папке media.

    ln -s /home/zdimon/Desktop/pl/data/ course

Создадим метод замены пути к картинкам в модели и применим его.

    class Topic(models.Model):
        ...

        @property
        def content(self):
            ...
            if os.path.isfile(path):
                f = open(path,'r')
                txt = f.read()
                txt = self.parse_subject_txt(txt)
                return parse_md(txt)
                f.close()
            else:
                return 'File %s does not exist!' % path
        ...
        def parse_subject_txt(self,txt):
            pathtosubject = '/media/course/%s/ru/%s' % (self.lesson.course.name_slug, self.lesson.name_slug)
            txt = txt.replace('{path-to-subject}',pathtosubject)
            return txt

# Страница урока.
 
Создаем роутинг pl/urls.py.

    from index.views import ... lesson_detail

    urlpatterns = [
        ...
        path('lesson/detail/<slug:slug>',lesson_detail, name="lesson_detail"),
        ...
    ]

Создаем функцию pl/index/views.py

    def lesson_detail(request,slug):
        lesson = Lesson.objects.get(name_slug=slug)
        return render(request,'lesson_detail.html',{'lesson': lesson})

Создаем медод get_absolute_url в модели.

    class Lesson(models.Model):
        ...

        def get_absolute_url(self):
            return reverse('lesson_detail', kwargs={'slug': self.name_slug })

Ставим ссылку в шаблон templates/course_detail.html.

    <ul class="lessons-list">
        {% for lesson in course.lesson_set.all %}
             <li><a href="{{ lesson.get_absolute_url }}">{{ lesson.title }}</a></li>
        {% endfor %}
     </ul>

Сам шаблон templates/lesson_detail.html

    {% extends 'layout.html' %}
    {% block carousel %} {% endblock %}
    {% block content %}

    <div class="section margin-top_50">
        <div class="container">
            <div class="row">
                <div class="col-md-12 layout_padding_2">
                    <div class="full">
                        <div class="heading_main text_align_left">
                           <h2>{{ lesson.title }}</h2>

                        </div>
                        {% for topic in lesson.topic_set.all %}
                            <div class="full">      
                                {{ topic.title }}
                            </div>   
                        {% endfor %}                 
                    </div>
                </div>
            </div>        
        </div>
    </div>

    {% endblock %}



Установка библиотеки markdown.

    pip install markdown

Создадим ф-цию конвертирования.

    import markdown

    def parse_md(txt):
        try:
            txt = txt.decode('UTF-8')
        except:
            pass
        return mark_safe(markdown.markdown(txt,extensions=['extra', 'smarty'], output_format='html5'))

Создадим в модели метод, возвращающий содержимое файла markdown статьи.

    from pl.settings import DATA_DIR
    import os

    ...
    class Topic(models.Model):


        @property
        def content(self):
            path = '%s/%s/ru/%s/%s' % (DATA_DIR,self.lesson.course.name_slug,self.lesson.name_slug,self.filename)
            #return path
            if os.path.isfile(path):
                f = open(path,'r')
                txt = f.read()
                return parse_md(txt)
                f.close()
            else:
                return 'File %s does not exist!' % path

Выведем в шаблоне.

        {% for topic in lesson.topic_set.all %}
            <div class="full">      

                {{ topic.content }}

            </div>   
        {% endfor %}    







