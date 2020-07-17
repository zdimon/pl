from django.db import models
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from django.urls import reverse
from pl.settings import DATA_DIR, ALL_FREE
import os


import markdown

from pl.settings import DATA_DIR, VIDEO_DIR
from os.path import isfile, join, isdir
from os import listdir

from bs4 import BeautifulSoup


def parse_md(txt):
    try:
        txt = txt.decode('UTF-8')
    except:
        pass
    return mark_safe(markdown.markdown(txt,extensions=['extra', 'smarty'], output_format='html5'))


class Course(models.Model):
    name = models.CharField(max_length=250, verbose_name=_(u'Name'), blank=True, null = True)
    desc = models.TextField(verbose_name=_(u'Description'), blank=True, null = True)
    image = models.ImageField(verbose_name=_(u'Image'), upload_to='course_images', blank=True, null = True)
    meta_keywords = models.TextField(blank=True, null = True)
    meta_title = models.CharField(max_length=255, blank=True, null = True)
    meta_description = models.TextField(blank=True, null = True)
    name_slug = models.CharField(verbose_name='Name slug',max_length=250, blank=True, null = True)
    is_active = models.BooleanField(verbose_name=_('Is published?'), default=False)

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.name_slug })

    def __str__(self):
        return self.name

    @property
    def image_tag(self):
        return mark_safe('<img width="60" src="%s" />' % self.image.url)

class Lesson(models.Model):
    title = models.CharField(max_length=250, blank=True, verbose_name=_(u'Name'))
    number = models.IntegerField(default=0, verbose_name=_(u'Number'))
    is_active = models.BooleanField(verbose_name=_('Is active?'), default=False)
    image = models.ImageField(blank=True, verbose_name=_(u'Image'), upload_to='lessons_images', null = True)
    course = models.ForeignKey(Course, verbose_name=_(u'Course'), on_delete=models.CASCADE)
    name_slug = models.CharField(verbose_name='Name slug',max_length=250, blank=True)
    desc = models.TextField(verbose_name=_(u'Description'), blank=True, null = True, default=' ')
    @property
    def get_image(self):
        path = '%s%s/%s/images/1.png' % (DATA_DIR,self.course.name_slug,self.name_slug)
        url = '/static/course/%s/%s/images/1.png' % (self.course.name_slug,self.name_slug)
        if isfile(path):
            # return path
            return mark_safe('<img width="150" src="%s" />' % url)
        else:
            return mark_safe('&nbsp;')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson_detail', kwargs={'slug': self.name_slug })


    def is_paid(self,user):
        if ALL_FREE:
            return True
        if self.number == 1:
            return True
        try:
            LessonPayments.objects.get(user=user,lesson=self, is_paid=True)
            return True
        except:
            return False

class Topic(models.Model):
    title = models.CharField(max_length=250, blank=True, verbose_name=_(u'Name'))
    filename = models.CharField(verbose_name='Name slug',max_length=250, blank=True)
    lesson = models.ForeignKey(Lesson, verbose_name=_(u'Lesson'), on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name=_(u'Course'), on_delete=models.CASCADE)
    video = models.CharField(verbose_name='Name slug',max_length=250, blank=True)
    has_video = models.BooleanField(default=False)
    is_youtube = models.BooleanField(default=False)

    @property
    def short_content(self):
        path = '%s/%s/%s/%s' % (DATA_DIR,self.lesson.course.name_slug,self.lesson.name_slug,self.filename)
        if os.path.isfile(path):
            f = open(path,'r')
            txt = f.read()
            txt = self.parse_subject_txt(txt)
            f.close()
            html =  parse_md(txt)
            soup = BeautifulSoup(html, 'html.parser')
            ps = soup.find_all('p')
            out = ''
            for p in ps[0:6]:
                out = out + str(p)
            return out
        else:
            return 'File %s does not exist!' % path

    @property
    def content(self):
        path = '%s/%s/%s/%s' % (DATA_DIR,self.lesson.course.name_slug,self.lesson.name_slug,self.filename)
        #return path
        if os.path.isfile(path):
            f = open(path,'r')
            txt = f.read()
            txt = self.parse_subject_txt(txt)
            return parse_md(txt)
            f.close()
        else:
            return 'File %s does not exist!' % path

    def __str__(self):
        return self.title

    def check_video(self,data):
        onlyfiles = [f for f in listdir(VIDEO_DIR) if isfile(join(VIDEO_DIR, f))]
        # print(data)
        
        if "youtube" in data:
            self.is_youtube = True
            self.video = data['youtube']
            self.has_video = True
            self.save()
            self.lesson.is_active = True
            self.lesson.save()
        else:
            for video in onlyfiles:
                fname = video.split('.')[0]
                if fname == self.filename.split('.')[0]:
                    self.has_video = True
                    self.video = video
                    self.has_video = True
                    self.save()
                    self.lesson.is_active = True
                    self.lesson.save()
        

    @property
    def video_tag(self):
        if self.is_youtube:
            out = '<iframe width="560" height="315" src="%s" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>' % self.video
            return mark_safe(out)
        if self.has_video:
            return mark_safe('<video  controls><source src="/static/video/%s" type="video/mp4"></video>' % self.video)
        else:
            return 'Видео отсутствует'


    def parse_subject_txt(self,txt):
        pathtosubject = '/media/course/%s/%s' % (self.lesson.course.name_slug, self.lesson.name_slug)
        txt = txt.replace('{path-to-subject}',pathtosubject)
        return txt


# PAYMENT MODEL

from django.contrib.auth.models import User

class LessonPayments(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null = True)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, blank=True, null = True)
    is_paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)   
  
################################   

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
