from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch # импортируем наше представление
 
 
urlpatterns = [
    # path — означает путь. В данном случае путь ко всем новостям у нас останется пустым
    path('', NewsList.as_view()), # т.к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', NewsDetail.as_view()),
    path('search', NewsSearch.as_view()),
]