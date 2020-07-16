# Установка PHP на Win 10
   
Скачиваем дистрибутив.

![admin]({path-to-subject}/images/1.png)

![admin]({path-to-subject}/images/2.png)

Распаковываем в папку с:/php

Переименовываем файл php.ini-production в php.ini

В нем раскоментируем строки 


    extension=curl
    extension=gd2
    extension=gettext
    extension=mbstring
    extension=mysqli
    extension=openssl
    extension=pdo_mysql
    extension=pdo_pgsql
    extension=pdo_sqlite
    extension=pgsql

Теперь нудно добавить путь c:/php в переменную окружения path.

Через поиск вводим env и ищем переменные окружения.

![admin]({path-to-subject}/images/3.png)

Уснанавливливаем композер.

[ссылка на скачивание](https://getcomposer.org/download/)

Создаем пороект Laraver.

    composer create-project --prefer-dist laravel/laravel blog

Скачиваем дистрибутив Apache.

[ссылка для скачивания](https://www.apachehaus.com/cgi-bin/download.plx)
 
Распаковываем архив в папку c:/apache

Открываем файл с:/apache/conf/httpd.conf и меняем следующее

    Define SRVROOT "c:/apache"

Добавляем php.

    PHPIniDir "c:/php"
    LoadModule php7_module "C:/php/php7apache2_4.dll"
    AddHandler application/x-httpd-php .php

Определяем виртуальный хост.

    <VirtualHost *:80>
        DocumentRoot "c:/Users/Dell/Desktop/php/blog/public"
        ServerName localhost
        <Directory "c:/Users/Dell/Desktop/php/blog/public">
                Options Indexes FollowSymLinks MultiViews
                AllowOverride All
                Require all granted
        </Directory>
    </VirtualHost>

Запускаем PowerShell от имени администратора и устанавливаем апач как сервис.

    cd C:\Apache24\bin
    .\httpd.exe -k install

Стартуем сервер.

    .\httpd.exe -k start

![admin]({path-to-subject}/images/4.png)

Устанавливаем MySQL.

[ссылка для скачивания](https://dev.mysql.com/downloads/installer/)

Прописываем коннект к базе в файле blog/.env



