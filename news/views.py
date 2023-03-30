#from django.shortcuts import render

#Создание внешнего представления
from django.views.generic import ListView, DetailView # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import News
 
 
class NewsList(ListView):
    model = News  # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты

# создаём представление, в котором будут детали конкретной отдельной новости
class NewsDetail(DetailView):
    model = News # модель всё та же, но мы хотим получать детали конкретной отдельной новости
    template_name = 'new.html' # название шаблона будет new.html
    context_object_name = 'new' # название объекта