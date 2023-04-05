from django.shortcuts import render
from django.core.paginator import Paginator # импортируем класс, позволяющий удобно осуществлять постраничный вывод


#Создание внешнего представления
from django.views.generic import ListView, DetailView # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import News
from .filters import NewsFilter # импортируем фильтр
from datetime import datetime
 
 
class NewsList(ListView):
    model = News  # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты
    queryset = News.objects.order_by('-id')
    paginate_by = 5
    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. 
    # В возвращаемом словаре context будут храниться все переменные. 
    # Ключи этого словари и есть переменные, к которым мы сможем потом обратиться через шаблон
    #забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['time_now'] = datetime.utcnow() # добавим переменную текущей даты time_now
        #context['value1'] = None # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context

# создаём представление, в котором будут детали конкретной отдельной новости
class NewsDetail(DetailView):
    model = News # модель всё та же, но мы хотим получать детали конкретной отдельной новости
    template_name = 'new.html' # название шаблона будет new.html
    context_object_name = 'new' # название объекта


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
    
