from django.contrib import admin
from django.utils.safestring import mark_safe
from course.models import Course, Lesson, Topic, LessonPayments, Comments, Subscription
from django.http import HttpResponse
from django.urls import reverse
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['image_tag', 'name_slug', 'desc', 'name', 'meta_title']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'name_slug', 'course', 'number', 'desc', 'is_active', 'subscribe_link']
    def subscribe_link(self, obj):
        url = reverse('admin:send_news',args=[obj.id])
        return mark_safe('<a href="%s">Разослать</a>' % url)

    def get_urls(self):
        from django.urls import path
        urls = super(LessonAdmin, self).get_urls()
        myurl = [
            path('send/news/<int:lesson_id>', self.admin_site.admin_view(self.send_news), name="send_news")
        ]
        return myurl+urls

    def send_news(self, request, lesson_id):
        lesson = Lesson.objects.get(pk=lesson_id)
        for s in Subscription.objects.all():
            print('Sent to %s' % s.email)
            title = 'Новый урок - %s' % lesson
            send_mail(
                title,
                title,
                'from@example.com',
                [s.email],
                fail_silently=False,
            )
        messages.success(request, 'Письма разослал')
        return redirect(reverse('admin:course_lesson_changelist'))


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'filename', 'course', 'lesson', 'video', 'has_video', 'is_youtube']



@admin.register(LessonPayments)
class LessonPaymentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'lesson', 'created', 'is_paid']



from mptt.admin import MPTTModelAdmin

@admin.register(Comments)
class CommentsAdmin(MPTTModelAdmin):
    list_display = ['user', 'content', 'parent']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['email']
