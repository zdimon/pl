## Фронтенд. 

### Angular и многопроектное окружение.

Мы будем создавать два приложения на Angular и разделять между ними один функционал из core приложения.

Поэтому целесообразно создать многопроектное окружение (с одним каталогом node_modules для всех).

[ссылка на документацию](https://github.com/ionic-team/ionic-cli/wiki/Angular-Monorepo)

### Создание окружения.

    ng new sdat --createApplication=false --directory=frontend

![start page]({path-to-subject}/images/1.png)


Меняем директорию и создаем новое приложение web для десктопа.

    cd frontend
    ng generate application web

При этом необходимо иметь установленным angular-cli чтобы работала команда ng.

![start page]({path-to-subject}/images/2.png)
    
Стартуем сервер.

    ng serve web

Создаем приложение для мобильных устройств на базе Ionic.

    ng generate application mobi

Создаем конфигурационный файл для Ionic

    ionic init --multi-app

Добавляем Ionic библиотеки.

    ng add @ionic/angular --project=mobi

И другие зависимости.

      "dependencies": {
        "@ionic/angular": "^5.1.1",
        "@ionic-native/core": "^5.0.7",
        "@ionic-native/splash-screen": "^5.0.0",
        "@ionic-native/status-bar": "^5.0.0",

Устанавливаем зависимости.

    npm install

В какой нибудь другой директории временно создадим шаблонный проект Ionic.

    ionic start myApp sidemenu

Заменим каталог mobi/src в нашем приложении  на тот же, но во временном шаблонном приложении myApp.

![start page]({path-to-subject}/images/3.png)


## Создадим новую библиотеку для предоставления общего функционала.


    ng generate library core --prefix=core

Запуск сборщика.
    
    ng build shareLib --watch


![start page]({path-to-subject}/images/4.png)


    
      
