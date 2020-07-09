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