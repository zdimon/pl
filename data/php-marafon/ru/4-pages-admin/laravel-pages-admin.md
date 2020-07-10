# Статичные страницы. Админка.

Создадим миграцию и добавим новое поле alias к станицам.

    php artisan make:migration add_alias_to_page_table

    // database/migrations/2020_06_22_112935_add_alias_to_page_table.php

    public function up()
    {
        Schema::table('page', function (Blueprint $table) {
            $table->string('alias');
        });
    }

Запуситим миграцию.

    php artisan migrate

Добавим alias в сеятель и скопируем картинки.

    DB::table('page')->insert([
        'title' => $item->title,
        'alias' => $item->alias,
        'content' => $item->content,
        'image' => $item->image
    ]);

    $file_path = base_path().'/fixture-data/images/posts/'.$item->image;
    $destination = base_path().'/public/storage/posts/'.$item->image;
    \File::copy($file_path,$destination);

Предварительно необходимо создать каталоги под картинки.

Так же в файл fixtures.json

    "pages": [
        {
            "title": "Dmitry Zharikov",
            "content": "Full stack developer",
            "image": "logo.jpg",
            "alias": "header"
        }, 
        {
            "title": "About me",
            "content": "PHP Python Javascript developer",
            "image": "my.jpg",
            "alias": "about_me"
        }        
    ],

Запуск сеятеля.

    php artisan db:seed --class=PageSeeder


Выбираем нужные записи в app/Providers/AppServiceProvider.php и передаем в шаблон.

    <?php

    namespace App\Providers;

    use Illuminate\Support\ServiceProvider;
    use Illuminate\Support\Facades\DB;
    use Illuminate\Support\Facades\View;

    class AppServiceProvider extends ServiceProvider
    {
        /**
         * Register any application services.
         *
         * @return void
         */
        public function register()
        {
            //
        }

        /**
         * Bootstrap any application services.
         *
         * @return void
         */
        public function boot()
        {
            $header = DB::table('page')->where('alias', 'header')->first();
            $about = DB::table('page')->where('alias', 'about_me')->first();
            View::share('header', $header);
            View::share('about', $about);
        }
    }

Выводим в шаблоне.

    <div class="container">                       
                <img class="profile-image img-responsive pull-left" width="150" src="storage/pages/{{ $header->image }}" alt="James Lee" />
                ....
        </header><!--//header-->
        
        <div class="container sections-wrapper">
            <div class="row">
                <div class="primary col-md-8 col-sm-12 col-xs-12">
                    <section class="about section">
                        <div class="section-inner">
                            <h2 class="heading">{{ $about->title }}</h2>
                            <div class="content">
                                <p>{{ $about->content }}</p>    
                            </div><!--//content-->
                        </div><!--//section-inner-->                 
                    </section><!--//section-->


![admin]({path-to-subject}/images/1.png)


## Форма авторизации resources/views/auth.blade.php.

    @extends('layout')

    @section('content')
        <form method="POST" action="login">
            @csrf
            Пароль: <input name="password" /> <input type="submit" value="Вход" />
        </form>
    @endsection

Роутинг.


Для формы.

    Route::get('/auth', function () {
        return view('auth');
    });

Для авторизации.
    
    use \Illuminate\Http\Request;
    ...
    Route::post('/', function (Request $request) {
        if($request->input('password') == '111') {
            $request->session()->put('is_auth', 'true');
        }
        return redirect('/');
    });

![admin]({path-to-subject}/images/2.png)

Проверяем авторизацию в шаблоне.

        @if(Session::has('is_auth'))
            <a class="btn btn-cta-primary pull-right" href="/pages">
                Редактирование страниц
            </a>
        @endif

![admin]({path-to-subject}/images/3.png)


Создадим контроллер для crud страниц.

    php artisan make:controller PageController --resource --model=Page

Добавив ресурсный маршрут.

    Route::resource('page','PageController');

![admin]({path-to-subject}/images/4.png)

Контроллер для списка страниц.

    public function index()
    {
        $pages = Page::all();
        return view('page.index')->with('pages', $pages);
    }

Шаблон для таблицы resources/views/page/index.blade.php


    @extends('layout')
     
    @section('content')
        
            <section class="about section">
                <div class="section-inner">   
       
                    <table class="table table-bordered">
                        <tr>
                            <th>No</th>
                            <th>Image</th>
                            <th>Alias</th>
                            <th>Title</th>
                            <th width="280px">Action</th>
                        </tr>
                        @foreach ($pages as $page)
                        <tr>
                            <td>{{ $page->id }}</td>
                            <td><img width="100" src="/storage/pages/{{ $page->image }}" /></td>
                            <td>{{ $page->alias }}</td>
                            <td>{{ $page->title }}</td>
                            <td>
                                <a class="btn btn-primary" href="{{ route('page.edit',$page->id) }}">Edit</a>
                            </td>
                        </tr>
                        @endforeach
                    </table>
                </div>
            </section>
          
    @endsection

![admin]({path-to-subject}/images/5.png)

Контролер для редактирования записи.

    public function edit(Page $page)
    {
        return view('page.edit',compact('page'));
    }

Шаблон для редактирования.

    @extends('layout')
       
    @section('content')
        <div class="row">
            <div class="col-lg-12 margin-tb">
                <div class="pull-left">
                    <h2>Редактирование</h2>
                </div>
                <div class="pull-right">
                    <a class="btn btn-primary" href="{{ route('page.index') }}"> Назад</a>
                </div>
            </div>
        </div>
       
      
        <form action="{{ route('page.update',$page->id) }}" method="POST" enctype="multipart/form-data">
            @csrf
            @method('PUT')
       
             <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12">
                    <div class="form-group">
                        <strong>Заголовок:</strong>
                        <input type="text" name="title" value="{{ $page->title }}" class="form-control" placeholder="Заголовок">
                    </div>
                </div>
                <div class="col-xs-12 col-sm-12 col-md-12">
                    <div class="form-group">
                        <strong>Изображение:</strong>
                        <input type="file" name="image" />
                    </div>
                </div>
                <div class="col-xs-12 col-sm-12 col-md-12">
                    <div class="form-group">
                        <strong>Описание:</strong>
                        <textarea class="form-control" style="height:150px" name="content" placeholder="Описание">{{ $page->content }}</textarea>
                    </div>
                </div>
                <div class="col-xs-12 col-sm-12 col-md-12 text-center">
                  <button type="submit" class="btn btn-primary">Сохранить</button>
                </div>
            </div>
       
        </form>
    @endsection


Прописываем поля для редактирования в модели.

    <?php

    namespace App;

    use Illuminate\Database\Eloquent\Model;

    class Page extends Model
    {
        protected $table = 'page';
        protected $fillable = ['title','content', 'image'];
    }

![admin]({path-to-subject}/images/6.png)


Контроллер для редактирования.

    public function update(Request $request, Page $page)
    {
        $page->update($request->all());
        $file = $request->file('image');
        $fileName = time().'.'.$file->extension();  
        $file->move(public_path('storage/pages'), $fileName);
        $page->image = $fileName;
        $page->save();
        return redirect()->route('page.index');
    }



