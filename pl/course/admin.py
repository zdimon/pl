from django.contrib import admin

from course.models import Course, Lesson, Topic, LessonPayments, Comments

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['image_tag', 'name_slug', 'desc', 'name', 'meta_title']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'name_slug', 'course', 'number', 'desc', 'is_active']

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
