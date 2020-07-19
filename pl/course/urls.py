from django.urls import path, include
from course.views import course_detail, lesson_detail, pay, my_cabinet, save_comment, discussion, subscribe
from course.views import articles
from course.views import article_detail
urlpatterns = [ 
    path('detail/<slug:slug>',course_detail, name="course_detail"),
    path('lesson/detail/<slug:slug>',lesson_detail, name="lesson_detail"),
    path('pay/<int:lesson_id>',pay, name="pay"),
    path('my/cabinet',my_cabinet, name="my_cabinet"),
    path('save/comment',save_comment, name="save_comment"),
    path('discussion',discussion, name="discussion"),
    path('subscribe',subscribe, name="subscribe"),
    path('articles',articles, name="articles"),
    path('article/<slug:slug>',article_detail, name="article_detail"),
]