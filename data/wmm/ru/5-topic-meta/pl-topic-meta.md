# Страница урока. Мета теги.
 
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


