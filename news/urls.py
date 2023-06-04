from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch, NewsCreateView, NewsUpdateView, NewsDeleteView, NewsCategoryView, subscribe_to_category, unsubscribe_to_category
from django.views.decorators.cache import cache_page
#from django.contrib.auth.decorators import login_required

 
urlpatterns = [
    # path — означает путь. В данном случае путь ко всем новостям у нас останется пустым
    path('', cache_page(60*1)(NewsList.as_view()), name = 'index'), # т.к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', NewsDetail.as_view(), name='new'),
    path('search', NewsSearch.as_view()),
    path('new_create/<int:pk>/', NewsCreateView.as_view(), name='new_create'),
    path('new_delete/<int:pk>/', NewsDeleteView.as_view(), name='new_delete'),
    path('new_update/<int:pk>/', NewsUpdateView.as_view(), name='new_update'),
    path('category/<int:pk>/', NewsCategoryView.as_view(), name='categories'),
    path('subscribe/<int:pk>/', subscribe_to_category, name='subscribe'),
    path('unsubscribe/<int:pk>/', unsubscribe_to_category, name='unsubscribe'),


]
