from django.contrib import admin

from course.models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['image_tag', 'name_slug', 'desc', 'name', 'meta_title']