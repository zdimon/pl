from django.urls import path, include
from .views import course_detail, lesson_detail, pay, my_cabinet

urlpatterns = [ 
    path('detail/<slug:slug>',course_detail, name="course_detail"),
    path('lesson/detail/<slug:slug>',lesson_detail, name="lesson_detail"),
    path('pay/<int:lesson_id>',pay, name="pay"),
    path('my/cabinet',my_cabinet, name="my_cabinet"),
]