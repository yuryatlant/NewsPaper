from django.db import models
from django.core.validators import MinValueValidator
 
# Создаём модель новостей 
class News(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True, # названия новостей не должны повторяться
    )
    description = models.TextField()
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news', # все новости в категории будут доступны через поле news
    )
    time_creation = models.DateTimeField(auto_now_add = True)
  
    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'
 
 
#  создаём категорию, к которой будет относиться новость
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # названия категорий тоже не должны повторяться
 
    def __str__(self):
        return f'{self.name.title()}'
