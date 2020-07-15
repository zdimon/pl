# Импорт видео.
    
Определим константу с путем к видео файлам.

    VIDEO_DIR = '/home/zdimon/Videos/course-data/ruslan'

Добавим поле с видео в модель.

    class Topic(models.Model):
        ...
        video = models.CharField(verbose_name='Name slug',max_length=250, blank=True)
        has_video = models.BooleanField(default=False)

Создадим и применим миграцию.

        ./manage.py makemigrations
        ./manage.py migrate

Доработаем класс импорта.

