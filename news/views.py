from django.shortcuts import render,redirect
from django.core.paginator import Paginator # импортируем класс, позволяющий удобно осуществлять постраничный вывод


#Создание внешнего представления
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView 
# импортируем классы в том представлении, что будут выводиться из БД
from .models import News,Category,UserCategory
from .filters import NewsFilter # импортируем фильтр
from .forms import NewsForm # импортируем форму
from datetime import datetime


#импорт для аутентификации
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives # импортируем класс для создание объекта письма с html
from django.template.loader import render_to_string # импортируем функцию, которая срендерит наш html в текст

from django.urls import resolve
from django.core.cache import cache # импортируем кэш

class NewsList(ListView):
    model = News  # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты
    queryset = News.objects.order_by('-id')
    paginate_by = 5
    form_class = NewsForm # добавляем форм класс, чтобы получать доступ к форме через метод POST
    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. 
    # В возвращаемом словаре context будут храниться все переменные. 
    # Ключи этого словари и есть переменные, к которым мы сможем потом обратиться через шаблон
    #забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['time_now'] = datetime.utcnow() # добавим переменную текущей даты time_now
        #context['value1'] = None # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        context['categories'] = Category.objects.all()
        context['form'] = NewsForm()
        return context
    def post(self, request, *args, **kwargs):
        # берём значения для нового товара из POST-запроса отправленного на сервер
        #name = request.POST['name']
        #description = request.POST['description']
        #category_id = request.POST['category']
         
        #new = News(name=name, description=description, category_id=category_id) # создаём новую новость и сохраняем
        #new.save()
        
        form = self.form_class(request.POST) # создаём новую форму, забиваем в неё данные из POST-запроса 
        if form.is_valid(): # если данные введены верно, то сохраняем новую новость
            form.save()

        # mailing = News(
        #     name=request.POST['name'],
        #     description=request.POST['description'],
        #     category=request.POST['category'])
        
        # html_content = render_to_string( 
        #     'mailing/notification.html',
        #     {'mailes': mailing }
        # )
        # msg = EmailMultiAlternatives(
        #     subject=f'{mailing.name}',
        #     body=mailing.description, #  это то же, что и message
        #     from_email='studium2002_1@mail.ru',
        #     to=['studium2002@mail.ru'], # это то же, что и recipients_list
        # )
        # msg.attach_alternative(html_content, "text/html") # добавляем html
        # msg.send() # отсылаем    
        
        return super().get(request, *args, **kwargs) # отправляем пользователя обратно на GET-запрос.    

# создаём представление, в котором будут детали конкретной отдельной новости
class NewsDetail(DetailView):
    model = News # модель всё та же, но мы хотим получать детали конкретной отдельной новости
    template_name = 'new.html' # название шаблона будет new.html
    context_object_name = 'new' # название объекта
    queryset = News.objects.all()
    def get_object(self, *args, **kwargs): # переопределяем метод получения объекта
        obj = cache.get(f'new-{self.kwargs["pk"]}', None) # кэш очень похож на словарь, и метод get действует также. Он забирает значение по ключу, если его нет, то забирает None.
 
        # если объекта нет в кэше, то получаем его и записываем в кэш
        if not obj:
            obj = super().get_object(queryset=self.queryset) 
            cache.set(f'new-{self.kwargs["pk"]}', obj)
        
        return obj

# дженерик для создания объекта. 
class NewsCreateView(CreateView):
    template_name = 'new_create.html'
    form_class = NewsForm
    

class NewsUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'new_create.html'
    form_class = NewsForm
    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return News.objects.get(pk=id)

# дженерик для удаления новости
class NewsDeleteView(DeleteView):
    template_name = 'new_delete.html'
    queryset = News.objects.all()
    success_url = '/news/'
    context_object_name = 'new_d'

class NewsSearch(ListView):
    model = News  # указываем модель, объекты которой мы будем выводить
    template_name = 'search.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты
    queryset = News.objects.order_by('id')
    
    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. 
    # В возвращаемом словаре context будут храниться все переменные. 
    # Ключи этого словари и есть переменные, к которым мы сможем потом обратиться через шаблон
    #забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context

class NewsCategoryView(ListView):
    model = News  
    template_name = 'category.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты
    ordering = ['-time_creation']
    paginate_by = 15
    #form_class = NewsForm
    def get_queryset(self):
        self.id = resolve(self.request.path_info).kwargs['pk']
        c = Category.objects.get(id=self.id)
        queryset = News.objects.filter(category=c)
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        category  = Category.objects.get(id=self.id)
        subscribed = category.subscribers.filter(email=user.email)
        if not subscribed: 
            context['sub'] = True
        else:
            context['sub'] = False
        context['category'] = category
        return context    

def subscribe_to_category(request,pk):
    user = request.user
    category = Category.objects.get(id=pk)
    if not category.subscribers.filter(id=user.id).exists():
        category.subscribers.add(user.id)
        email = user.email
        html_content = render_to_string (
            'mailing/subscribed.html',
            {
                'categories': category,
                'user' : user,
            },
        )
        msg = EmailMultiAlternatives(
            subject=f'Подтверждение подписи на категорию - {category}',
            body='',
            from_email='studium2002_1@mail.ru',
            to=[email,], # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html") # добавляем html
        try:
            msg.send() # отсылаем  
        except Exception as e:
            print(e)
        return redirect('index')
    return redirect(request.Meta.get('HTTP_REFERER'))

def unsubscribe_to_category(request,pk):
    user = request.user
    category = Category.objects.get(id=pk)
    if category.subscribers.filter(id=user.id).exists():
        category.subscribers.remove(user.id)
    return redirect('index')