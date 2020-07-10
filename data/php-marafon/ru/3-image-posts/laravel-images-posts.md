# Загрузка картинок, вывод постов.

Создаем каталог с картинками и меняем их имена в fixtures.json
       
![start page]({path-to-subject}/images/1.png)

Создаем ссылку на файловое хранилище.

    php artisan storage:link

![start page]({path-to-subject}/images/2.png)

Изменяем класс PostSeeder.

    <?php
    ...
    class PostSeeder extends Seeder
    {
       ...
        public function run()
        {
            ...
            foreach($data->posts as $item){
                ...
                $file_path = base_path().'/fixture-data/images/posts/'.$item->image;
                $destination = base_path().'/public/storage/posts/'.$item->image;
                \File::copy($file_path,$destination);

            }
        }
    }

Определяем в layout центральный блок.

    @section('content')
        
    @show

Создаем контроллер для главной страницы.

    php artisan make:controller IndexController

Определяем метод.

    <?php

    namespace App\Http\Controllers;

    use Illuminate\Http\Request;

    class IndexController extends Controller
    {
        public function index()
        {
            return view('index');
        }

    }

Подключаем в роутинг.

    Route::get('/', 'IndexController@index');

Создаем шаблон resources/views/index.blade.php.

    @extends('layout')

    @section('content')
        <section class="latest section">
                <div class="section-inner">
                    <h2 class="heading">Latest Projects</h2>
                    <div class="content">    
                         
                    @foreach ($posts as $post)

                        <hr class="divider" />
                        <div class="item row">
                            <a class="col-md-4 col-sm-4 col-xs-12" href="#" target="_blank">
                            <img class="img-responsive project-image" src="storage/posts/{{ $post->image }}" alt="project name" />
                            </a>
                            <div class="desc col-md-8 col-sm-8 col-xs-12">
                                <h3 class="title">
                                    <a href="#" target="_blank">
                                    {{ $post->title }}
                                    </a></h3>
                                <p>{{ $post->content }}</p>
                                
                            </div><!--//desc-->                          
                        </div><!--//item-->
                        
                    @endforeach                            
                        
                        
                    </div><!--//content-->  
                </div><!--//section-inner-->                 
            </section><!--//section-->

    @endsection



Выбираем записи.

    <?php

    namespace App\Http\Controllers;

    use Illuminate\Http\Request;
    use App\Post;

    class IndexController extends Controller
    {
        public function index()
        {
            $posts = Post::all();
            return view('index',['posts'=>$posts]);
        }

    }

![start page]({path-to-subject}/images/3.png)



