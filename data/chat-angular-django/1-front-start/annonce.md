# Социальная сеть знакомств. Чат.

Цель проекта: создать одностраничное приложение для мобильных устройств, используя Django на серверной части и Angular Ionic на клиентской.

## Базовый функционал сайта.


Простая регистрация через форму и Google Auth.

Редактирование профиля и загрузка медиа-контента.

Создание блога с медиа-контентом.

Чат в реальном времени. 

Трансляция видео через WebRTC. 

Вывод пользователей в онлайне и контактов (с теми с кем была переписка). 

Получение уведомлений в реальном времени о разных событиях.

Поиск профилей.

## Коммерческий функционал.

Пополнение баланса мужчиной.

Снятие кредитов за различные услуги на сайте.

Просмотр истории платежей.

Начисление коммисионных девушкам.


## Архитектура.

Проект имеет монолитную структуру и все содержится в одном репозитории.

### Фронтенд Angular (JS TypeScript).

1. web приложение (чистый Angular) для десктопа

2. мобильное приложение (Ionic + Angular) 

3. core приложение для общих модулей, сервисов, компонентов и т.д.

### Бекенд Python.

Django Rest Framework - для построения REST API

Django channels - для отслеживания пользователей онлайн по web-sockets

Django celery - для отложенных задач

WebRTC - для трансляции видео и аудио потока

Centrifugo - сервер для передачи сообщений по веб-сокетам.





















