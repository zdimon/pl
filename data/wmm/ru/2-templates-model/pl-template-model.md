# Шаблонный синтаксис. Модели.
   
Определяем главный шаблон templates/layout.html и помечаем, блоки которые будем переопределять в дочерних шаблонах.

    <!DOCTYPE html>
    <html lang="en">
    <!-- Basic -->

    <head>
        ...

    </head>

    <body id="home" data-spy="scroll" data-target="#navbar-wd" data-offset="98">

        
        <header class="top-header">
            ...
        </header>
        <!-- End header -->

        <!-- Start Banner -->
        {% block carousel %}
        <div class="ulockd-home-slider">
            <div class="container-fluid">
                <div class="row">
                    ...
                      
                    </div>
                    <!-- .pogoSlider -->
                </div>
            </div>
        </div>
        {% endblock %}


        {% block content %} {% endblock %}

	    
        <footer class="footer-box">
            ...
        </footer>
        <!-- End Footer -->

        {% include 'copyright.html' %}

        ...

    </body>

    </html>

Конструкция {% include 'copyright.html' %} просто включает сторонний шаблон внутрь.

Теперь определяем дочерний шаблон index.html и наследуем его от базового.

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
                           <a class="hvr-radial-out button-theme" href="{{ course.get_absolute_url }}">Подробней</a>
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

При это переопределяеб блоки content и carousel.

## Модель данных.

Определяем модель данных для страниц index/models.py.

    from django.db import models


    class Page(models.Model):
        title = models.CharField(max_length=250)
        content = models.TextField(default='undefined')
        image = models.ImageField(upload_to='pages')

        def __str__(self):
            return self.title

Создаем миграцию.

    ./manage.py makemigration

Применяем миграцию.

    ./manage.py migrate

Создаем класс админки index/admin.py.

    from django.contrib import admin
    from index.models import Page

    @admin.register(Page)
    class PageAdmin(admin.ModelAdmin):
        list_display = ['title', 'content']
        search_fields = ['title']

## Установка темы админки grapelli.

[ссылка на официальный сайт](https://grappelliproject.com/)

[установка](https://django-grappelli.readthedocs.io/en/latest/quickstart.html#installation)    

![admin]({path-to-subject}/images/1.png)

## Создаем команду загрузки страниц в БД index/management/commands/load_pages.py.


    from django.core.management.base import BaseCommand, CommandError
    from index.models import Page

    class Command(BaseCommand):
      
        def handle(self, *args, **options):
            print('Start command')
            Page.objects.all().delete()
            p = Page()
            p.title = 'title 1'
            p.content = 'content '
            p.save()

Запуск команды.

    ./manage.py load_pages

