from django.contrib import admin

from course.models import Course, Lesson, Topic, LessonPayments

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['image_tag', 'name_slug', 'desc', 'name', 'meta_title']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'name_slug', 'course', 'number']

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'filename', 'lesson', 'video', 'has_video']


@admin.register(LessonPayments)
class LessonPaymentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'lesson', 'created', 'is_paid']
