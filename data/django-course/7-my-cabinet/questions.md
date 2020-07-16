# Вопросы, комментарии.
      
Создадим модель для вопросов.

При этом воспользуемся библиотекой mptt.

[ссылка на документацию](https://django-mptt.readthedocs.io/en/latest/index.html)

Устанавливаем.

    pip install django-mptt

Прописываем в настройках.

    INSTALLED_APPS = [
    ...
        'mptt'
    ]

Создаем модель.

    from mptt.models import MPTTModel, TreeForeignKey

    class Comments(MPTTModel):
        content = models.TextField()
        user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null = True)
        parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
        created = models.DateTimeField(auto_now_add=True)
        class MPTTMeta:
            order_insertion_by = ['user']

Проводим миграцию.

Выводим форму под уроком.


    <div class="section contact_section" style="background:#12385b;">
        <div class="container">
            <div class="row">
                
                <div class="layout_padding col-lg-12 col-md-12 col-sm-12">
                    <div class="contact_form">
                        <span class="white-title">Задать вопрос, прокомментировать.</span>
                        <form action="contact.html">
                        <fieldset>
                            
                            <div class="full field">
                                <textarea placeholder="Massage"></textarea>
                            </div>
                            <div class="full field">
                                <div class="center"><button>Отправить</button></div>
                            </div>
                        </fieldset>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>