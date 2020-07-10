# Ставим шаблон. Наполняем базу данных.

[ссылка на репозиторий](https://github.com/zdimon/laravel-blog)

[ссылка на бесплатные шаблоны](https://themes.3rdwavemedia.com/)

Переименуем resources/views/welcome.blade.php 

в

resources/views/layout.blade.php 

Изменим имя шаблона в routes/web.php.

    Route::get('/', function () {
        return view('layout');
    });

Вставляем шаблон в resources/views/layout.blade.php

    <!DOCTYPE html>
    <!--[if IE 8]> <html lang="en" class="ie8"> <![endif]-->  
    <!--[if IE 9]> <html lang="en" class="ie9"> <![endif]-->  
    <!--[if !IE]><!--> <html lang="en"> <!--<![endif]-->  
    <head>
        <title>Responsive Portfolio Template for Developers</title>
        <!-- Meta -->
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="Responsive HTML5 Website Landing Page for Developers">
        <meta name="author" content="Xiaoying Riley at 3rd Wave Media">    
        <link rel="shortcut icon" href="favicon.ico">  
        <link href='http://fonts.googleapis.com/css?family=Lato:300,400,300italic,400italic' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Montserrat:400,700' rel='stylesheet' type='text/css'> 
        <!-- Global CSS -->
        <link rel="stylesheet" href="assets/plugins/bootstrap/css/bootstrap.min.css">   
        <!-- Plugins CSS -->
        <link rel="stylesheet" href="assets/plugins/font-awesome/css/font-awesome.css">
        
        <!-- github calendar css -->
        <link rel="stylesheet" href="assets/plugins/github-calendar/dist/github-calendar.css"
    />
        <!-- github acitivity css -->
        <link rel="stylesheet" href="assets/plugins/github-activity/src/github-activity.css">
        <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/octicons/2.0.2/octicons.min.css">
        
        <!-- Theme CSS -->  
        <link id="theme-style" rel="stylesheet" href="assets/css/styles.css">
        <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
        <!--[if lt IE 9]>
          <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
          <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        <![endif]-->
        
    </head> 

    <body>
        <!-- ******HEADER****** --> 
        <header class="header">
            <div class="container">                       
                <img class="profile-image img-responsive pull-left" src="assets/images/profile.png" alt="James Lee" />
                <div class="profile-content pull-left">
                    <h1 class="name">James Lee</h1>
                    <h2 class="desc">Web App Developer</h2>   
                    <ul class="social list-inline">
                        <li><a href="#"><i class="fa fa-twitter"></i></a></li>                   
                        <li><a href="#"><i class="fa fa-google-plus"></i></a></li>
                        <li><a href="#"><i class="fa fa-linkedin"></i></a></li>
                        <li><a href="#"><i class="fa fa-github-alt"></i></a></li>                  
                        <li class="last-item"><a href="#"><i class="fa fa-hacker-news"></i></a></li>                 
                    </ul> 
                </div><!--//profile-->
                <a class="btn btn-cta-primary pull-right" href="http://themes.3rdwavemedia.com/" target="_blank"><i class="fa fa-paper-plane"></i> Contact Me</a>              
            </div><!--//container-->
        </header><!--//header-->
        
        <div class="container sections-wrapper">
            <div class="row">
                <div class="primary col-md-8 col-sm-12 col-xs-12">
                    <section class="about section">
                        <div class="section-inner">
                            <h2 class="heading">About Me</h2>
                            <div class="content">
                                <p>Write a brief intro about yourself</p>    
                            </div><!--//content-->
                        </div><!--//section-inner-->                 
                    </section><!--//section-->
        
                   <section class="latest section">
                        <div class="section-inner">
                            <h2 class="heading">Latest Projects</h2>
                            <div class="content">    
                                                   

                                <hr class="divider" />
                                <div class="item row">
                                    <a class="col-md-4 col-sm-4 col-xs-12" href="http://themes.3rdwavemedia.com/website-templates/responsive-bootstrap-theme-mobile-apps-atom/" target="_blank">
                                    <img class="img-responsive project-image" src="assets/images/projects/project-5.png" alt="project name" />
                                    </a>
                                    <div class="desc col-md-8 col-sm-8 col-xs-12">
                                        <h3 class="title"><a href="http://themes.3rdwavemedia.com/website-templates/responsive-bootstrap-theme-mobile-apps-atom/" target="_blank">Atom - Designed for Mobile Apps</a></h3>
                                        <p>You can put one of your secondary projects here. Suspendisse in tellus dolor. Vivamus a tortor eu turpis pharetra consequat quis non metus. Aliquam aliquam, orci eu suscipit pellentesque, mauris dui tincidunt enim, eget iaculis ante dolor non turpis.</p>
                                        <p><a class="more-link" href="http://themes.3rdwavemedia.com/website-templates/responsive-bootstrap-theme-mobile-apps-atom/" target="_blank"><i class="fa fa-external-link"></i> Find out more</a></p>
                                    </div><!--//desc-->                          
                                </div><!--//item-->
                                
                                                      
                               
                                
                            </div><!--//content-->  
                        </div><!--//section-inner-->                 
                    </section><!--//section-->
                    


                </div><!--//primary-->
                <div class="secondary col-md-4 col-sm-12 col-xs-12">

                    <aside class="list music aside section">
                        <div class="section-inner">
                            <h2 class="heading">Categories</h2>
                            <div class="content">
                                <ul class="list-unstyled">
                                    <li><i class="fa fa-headphones"></i> <a href="#">Python</a></li>
                                    <li><i class="fa fa-headphones"></i> <a href="#">Javascript</a></li>
                                    <li><i class="fa fa-headphones"></i> <a href="#">PHP</a></li>
                                </ul>
                            </div><!--//content-->
                        </div><!--//section-inner-->
                    </aside><!--//section-->
                    
                    <aside class="blog aside section">
                        <div class="section-inner">
                            <h2 class="heading">Latest Blog Posts</h2>
                            <p>You can use Sascha Depold's <a href="https://github.com/sdepold/jquery-rss" target="_blank">jQuery RSS plugin</a> to pull in your blog post feeds.</p>
                            <div id="rss-feeds" class="content">

                            </div><!--//content-->
                        </div><!--//section-inner-->
                    </aside><!--//section-->
                    

                  
                </div><!--//secondary-->    
            </div><!--//row-->
        </div><!--//masonry-->
        
        <!-- ******FOOTER****** --> 
        <footer class="footer">
            <div class="container text-center">
                    <!--/* This template is released under the Creative Commons Attribution 3.0 License. Please keep the attribution link below when using for your own project. Thank you for your support. :) If you'd like to use the template without the attribution, you can check out other license options via our website: themes.3rdwavemedia.com */-->
                    <small class="copyright">Designed with <i class="fa fa-heart"></i> by <a href="http://themes.3rdwavemedia.com" target="_blank">Xiaoying Riley</a> for developers</small>
            </div><!--//container-->
        </footer><!--//footer-->
     
        <!-- Javascript -->          
        <script type="text/javascript" src="assets/plugins/jquery-1.11.3.min.js"></script>
        <script type="text/javascript" src="assets/plugins/bootstrap/js/bootstrap.min.js"></script>    
        <script type="text/javascript" src="assets/plugins/jquery-rss/dist/jquery.rss.min.js"></script> 
        <!-- github calendar plugin -->
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/es6-promise/3.0.2/es6-promise.min.js"></script>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/fetch/0.10.1/fetch.min.js"></script>
        <script type="text/javascript" src="assets/plugins/github-calendar/dist/github-calendar.min.js"></script>
        <!-- github activity plugin -->
        <script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/mustache.js/0.7.2/mustache.min.js"></script>
        <script type="text/javascript" src="assets/plugins/github-activity/src/github-activity.js"></script>
        <!-- custom js -->
        <script type="text/javascript" src="assets/js/main.js"></script>            
    </body>
    </html> 

Копируем из шаблона папку assets в public.


![admin]({path-to-subject}/images/1.png)

Создаем миграцию для страниц.

    php artisan make:migration create_page_table

Создаем мишрацию для категорий

    php artisan make:migration create_category_table

Создаем миграцию для постов.

    php artisan make:migration create_post_table

![admin]({path-to-subject}/images/2.png)

Заполняем структуру таблицы для страниц database/migrations/<datetime>_create_page_table.php.

    public function up()
    {
        Schema::create('page', function (Blueprint $table) {
            $table->id();
            $table->timestamps();
            $table->string('title');
            $table->string('image');
            $table->text('content');
        });
    }

Для категорий.

    public function up()
    {
        Schema::create('category', function (Blueprint $table) {
            $table->id();
            $table->timestamps();
            $table->string('name');
        });
    }

Для постов.


    public function up()
    {
        Schema::create('post', function (Blueprint $table) {
            $table->id();
            $table->timestamps();
            $table->string('title');
            $table->string('image');
            $table->text('content');
        });
    }

Применяем миграцию.

    php artisan migrate

![admin]({path-to-subject}/images/3.png)

![admin]({path-to-subject}/images/4.png)


Создаем файл с фикстурами (тестовыми данными) fixture.json со страницами.

    {
        "pages": [
            {
                "title": "Test title 1",
                "content": "Test content 1",
                "image": "image1.jpg"
            }, 
            {
                "title": "Test title 2",
                "content": "Test content 2",
                "image": "image2.jpg"
            }        
        ]
    }

Создаем модель под страницы, категори и посты.

    php artisan make:model Page
    php artisan make:model Category
    php artisan make:model Post

Прописывем таблицы в каждом классе модели в каталоге app.

    <?php

    namespace App;

    use Illuminate\Database\Eloquent\Model;

    class Category extends Model
    {
        protected $table = 'category';
    }


    <?php

    namespace App;

    use Illuminate\Database\Eloquent\Model;

    class Page extends Model
    {
        protected $table = 'page';
    }

    <?php

    namespace App;

    use Illuminate\Database\Eloquent\Model;

    class Post extends Model
    {
        protected $table = 'post';
    }



![admin]({path-to-subject}/images/7.png)

## Загрузка страниц.

Создаем сеятеля для станиц.

    php artisan make:seeder PageSeeder

![admin]({path-to-subject}/images/5.png)

Заполняем таблицу данными из fixtures.json в database/seeds/PageSeeder.php

    <?php

    use Illuminate\Database\Seeder;
    use App\Page;
    class PageSeeder extends Seeder
    {
        /**
         * Run the database seeds.
         *
         * @return void
         */
        public function run()
        {
            $path = base_path().'/fixtures.json';
            $content = file_get_contents($path);
            $data = json_decode($content);
            Page::truncate();
            foreach($data->pages as $item){
                echo "Inserting ".$item->title."\n";
                DB::table('page')->insert([
                    'title' => $item->title,
                    'content' => $item->content,
                    'image' => $item->image
                ]);
            }

        }
    }

Альтернативный способ создания записи.

    $page = new Page();
    $page->title = $item->title;
    $page->content = $item->content;
    $page->image = $item->image;
    $page->save();


Обновляем автозагрузчик.

    composer dump-autoload

![admin]({path-to-subject}/images/6.png)

Запуск сеятеля.

    php artisan db:seed --class=PageSeeder

# Загрузка категорий.

Добавляем категории в фикстуры.

    {
        "pages": [
            ...        
        ],
        "categories": [
            {
                "name": "PHP"
            }, 
            {
                "name": "Python"
            }, 
            {
                "name": "Javascript"
            }    
        ]
    }

Класс сеятеля.
    
    php artisan make:seeder CategorySeeder

Сеим таблицу категорий.

    php artisan db:seed --class=CategorySeeder

![admin]({path-to-subject}/images/8.png)

# Загрузка постов.

Добавляем посты в фикстуры.

    {
        "pages": [
            ...     
        ],
        "categories": [
           ...    
        ],

        "posts": [
            {
                "title": "Title about PHP",
                "image": "image_post1.jpeg",
                "content": "Content about PHP",
                "category": "PHP"
            }, 
            {
                "title": "Title about Python",
                "image": "image_post1.jpeg",
                "content": "Content about Python",
                "category": "PHP"
            }, 
            {
                "title": "Title about Javascript",
                "image": "image_post1.jpeg",
                "content": "Content about Javascript",
                "category": "PHP"
            }    
        ]
    }

Создаем класс сеятеля.

    php artisan make:seeder PostSeeder

    php artisan migrate:reset

Добавим внешний ключ в схему с постами.


        Schema::create('post', function (Blueprint $table) {
            ...
            $table->unsignedBigInteger('category_id');
            $table->foreign('category_id')->references('id')->on('category')->onDelete('cascade'); 
        });

Создаем логику засеивания.

    <?php

    use Illuminate\Database\Seeder;
    use Illuminate\Support\Facades\DB;
    use App\Category;
    use App\Post;
    class PostSeeder extends Seeder
    {
        /**
         * Run the database seeds.
         *
         * @return void
         */
        public function run()
        {
            $path = base_path().'/fixtures.json';
            $content = file_get_contents($path);
            $data = json_decode($content);
            Post::truncate();
            foreach($data->posts as $item){
                echo "Inserting ".$item->title."\n";
                $cat = DB::table('category')->where('name', $item->category)->first();
                
                DB::table('post')->insert([
                    'title' => $item->title,
                    'content' => $item->content,
                    'image' => $item->image,
                    'category_id' => $cat->id
                ]);
            }
        }
    }


Засеиваем.

    php artisan db:seed --class=PostSeeder

![admin]({path-to-subject}/images/10.png)

Меняем 

    Category::truncate();

на

    DB::table('category')->delete();
    


![admin]({path-to-subject}/images/9.png)


