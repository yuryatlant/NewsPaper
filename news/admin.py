from django.contrib import admin
from .models import Category, News
 

# Регистрируем модель
 
admin.site.register(Category)
admin.site.register(News)