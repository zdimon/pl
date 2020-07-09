# Импорт курсов.

Создадим новое приложение и включим его в INSTALLED_APPS.

    ./manage.py startapp course

Создадим модель для таблицы курсов.

    from django.db import models
    from django.utils.translation import ugettext as _

    class Course(models.Model):
        name = models.CharField(max_length=250, verbose_name=_(u'Name'), blank=True, null = True)
        desc = models.TextField(verbose_name=_(u'Description'), blank=True, null = True)
        image = models.ImageField(verbose_name=_(u'Image'), upload_to='course_images', blank=True, null = True)
        meta_keywords = models.TextField(blank=True, null = True)
        meta_title = models.CharField(max_length=255, blank=True, null = True)
        meta_description = models.TextField(blank=True, null = True)
        name_slug = models.CharField(verbose_name='Name slug',max_length=250, blank=True, null = True)
        is_active = models.BooleanField(verbose_name=_('Is published?'), default=False)


Создадим и применим миграцию.

![admin]({path-to-subject}/images/1.png)

Админка.

    from django.contrib import admin

    from course.models import Course

    @admin.register(Course)
    class CourseAdmin(admin.ModelAdmin):
        list_display = ['name_slug', 'desc', 'name', 'meta_title']

Создадим команду для загрузки курсов course/management/commands/load_course.py.

    from django.core.management.base import BaseCommand, CommandError
    from course.models import Course

    class Command(BaseCommand):
      
        def handle(self, *args, **options):
            print('Start loading courses')
           
Запуск команды.

    ./manage.py load_course

Определяем в настойках путь к данным.

    DATA_DIR = str(os.path.join(BASE_DIR, "../data"))

Создадим класс-загрузчик для курсов.

    from course.models import  Course
    from pl.settings import DATA_DIR
    from os import listdir
    from os.path import isfile, join, isdir

    class CourseLoader(object):

        def __init__(self, *args, **kwargs):
            self.dir = args[0]

        def process(self):
            self.get_course_or_create()

        def get_course_or_create(self):
            try: 
                self.course = Course.objects.get(name_slug=self.dir)
            except:
                self.course = Course()
                self.course.name_slug = self.dir
                self.course.save()

        @staticmethod
        def get_active_courses_dirs():
            out = []
            onlydirs = [f for f in listdir(DATA_DIR) if isdir(join(DATA_DIR, f))]
            for d in onlydirs:
                if d.find('.') == -1:
                    out.append(d)
            return out

Вызовем метод в команде.

    from django.core.management.base import BaseCommand, CommandError
    from course.models import Course
    from course.course_loader import CourseLoader
    from pl.settings import DATA_DIR

    class Command(BaseCommand):
      
        def handle(self, *args, **options):
            print('Start loading courses from %s' % DATA_DIR)
            for d in CourseLoader.get_active_courses_dirs():
                loader = CourseLoader(d)
                loader.process()

Заберем и сохраним мета информацию.

    import yaml

    class CourseLoader(object):

       ...
        def process(self):
            self.get_course_or_create()
            self.save_meta_course()

        ...
        def save_meta_course(self):
            path = DATA_DIR+'/'+self.dir+'/meta.yml'
            print('Saving meta for %s' % self.course.name_slug)
            meta = self.get_meta(path)
            self.course.name = meta['title_ru']
            self.course.meta_keywords = meta['meta_keywords_ru']
            self.course.meta_title = meta['meta_title_ru']
            self.course.meta_description = meta['meta_description_ru']
            self.course.desc = meta['desc_ru']
            self.course.save()

        ...

        def get_meta(self,path):
            if isfile(path):
                f = open(path,'r')
                str = f.read()
                f.close()
                yml = yaml.load(str, Loader=yaml.FullLoader)
                return yml
            else:
                return False

Load image.

        
    from django.core.files import File

    class CourseLoader(object):

       ...
        def save_meta_course(self):
          ...
            try:
                im_path = DATA_DIR+'/'+self.dir+'/image.png'
                print('Loading image %s' % im_path)
                with open(im_path,'rb') as img_file:
                    self.course.image.save('image.png', File(img_file), save=True)
            except Exception as e:
                print(str(e))

Output image.

    from django.utils.safestring import mark_safe

    class Course(models.Model):
        ...
        @property
        def image_tag(self):
            return mark_safe('<img width="60" src="%s" />' % self.image.url)

Admin.

    class CourseAdmin(admin.ModelAdmin):
        list_display = ['image_tag', ...]

![admin]({path-to-subject}/images/2.png)


