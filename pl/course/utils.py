from course.models import Lesson, NewsLetter


def make_news_letter():
    lessons = []
    for l in Lesson.objects.filter(is_new=True):
        cont = '''
          <p><a href="%s"> %s </a></p>
        ''' % (l.get_absolute_url, l.title)
        lessons.append(cont)
        #l.is_new = False
        #l.save()
    nl = NewsLetter()
    nl.title = 'Новые уроки на webmonstr.com'
    nl.content = '<br />'.join(lessons)
    nl.save()
    