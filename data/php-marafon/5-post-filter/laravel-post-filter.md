# Последние посты. Фильтр.

Выбираем последние 3 поста из базы и категории в app/Providers/AppServiceProvider.php

    <?php
    ...
    use \App\Post;
    use \App\Category;

    class AppServiceProvider extends ServiceProvider
    {
        ...
        public function boot()
        {
            ...
            $last_posts = Post::orderBy('created_at', 'desc')->paginate(3);
            $categories = Category::all();

            ...

            View::share('last_posts', $last_posts);
            View::share('categories', $categories);

        }
    }



Выводим в шаблоне.

                <aside class="list music aside section">
                    <div class="section-inner">
                        <h2 class="heading">Категории</h2>
                        <div class="content">
                            <ul class="list-unstyled">
                                @foreach ($categories as $category)
                                    <li><i class="fa fa-headphones"></i> <a href="#">
                                        {{ $category->name }}
                                    </a></li>
                                @endforeach
                            </ul>
                        </div><!--//content-->
                    </div><!--//section-inner-->
                </aside><!--//section-->
                
                <aside class="blog aside section">
                    <div class="section-inner">
                        <h2 class="heading">Последние посты</h2>
                        @foreach ($last_posts as $post)
                            <div id="rss-feeds" class="content">
                                <div class="item">
                                    <h3 class="title" style="">
                                        <a target="_blank">
                                            {{ $post->title }}
                                        </a>
                                    </h3>
                                    
                                </div>           
                            </div><!--//content-->
                        @endforeach
                    </div><!--//section-inner-->
                </aside><!--//section-->

Убираем из шаблона ajax подгрузку.

    <script type="text/javascript" src="/assets/js/main.js"></script>      


![start page]({path-to-subject}/images/1.png)

Добавим больше постов в фикстуры.

    "posts": [
        {
            "title": "Title about PHP 1",
            "image": "1.png",
            "content": "Content about PHP",
            "category": "PHP"
        }, 
        {
            "title": "Title about Python 1",
            "image": "2.png",
            "content": "Content about Python",
            "category": "Python"
        }, 
        {
            "title": "Title about Javascript 1",
            "image": "3.png",
            "content": "Content about Javascript",
            "category": "Javascript"
        },
        {
            "title": "Title about PHP 2",
            "image": "1.png",
            "content": "Content about PHP",
            "category": "PHP"
        }, 
        {
            "title": "Title about Python 2",
            "image": "2.png",
            "content": "Content about Python",
            "category": "Python"
        }, 
        {
            "title": "Title about Javascript 2",
            "image": "3.png",
            "content": "Content about Javascript",
            "category": "Javascript"
        }    
    ]

Загрузим их еще раз.

    php artisan db:seed --class=PostSeeder

Создадим контроллер для фильтра.

    php artisan make:controller FilterController

Содержимое контроллера.

    <?php

    namespace App\Http\Controllers;

    use Illuminate\Http\Request;
    use App\Post;


    class FilterController extends Controller
    {
        public function index($id)
        {
            $posts = Post::where('category_id', $id)->get();
            return view('index')->with('posts', $posts);

        }    
    }


Добавляем маршрут.

    Route::get('/filter/{id}', 'FilterController@index');

![start page]({path-to-subject}/images/2.png)

Выводим в шаблоне ссылку на маршрут.

    @foreach ($categories as $category)
        <li><i class="fa fa-headphones"></i> 
        <a href="/filter/{{ $category->id }}">
            {{ $category->name }}
        </a></li>
    @endforeach



Шаблон для вывода статей.

    @extends('layout')

    @section('content')
        <section class="latest section">
                <div class="section-inner">
                    <h2 class="heading">Статьи</h2>
                    <div class="content">    
                         
                    @foreach ($posts as $post)

                        <hr class="divider" />
                        <div class="item row">
                            <a class="col-md-4 col-sm-4 col-xs-12" href="#" target="_blank">
                            <img class="img-responsive project-image" src="/storage/posts/{{ $post->image }}" alt="project name" />
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




![start page]({path-to-subject}/images/3.png)





