# Кабинет пользователя.
    
Создаем вьюху под кабинет.

    @login_required
    def my_cabinet(request):
        payments = LessonPayments.objects.filter(user=request.user).order_by('-id')
        return render(request,'my_cabinet.html',{'payments': payments})

Добавляем в роутинг.

