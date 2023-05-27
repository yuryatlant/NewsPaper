# Create your models here.
from django.db import models
from news.models import Category
from django.contrib.auth.models import Group

from django import forms
from allauth.account.forms import SignupForm

class BasicSignupForm(SignupForm):
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        #добавили базовую категорию
        basic_category = Category.objects.get(name='Наука')
        basic_category.subscribers.add(user)
        return user
    
    
#from django.contrib.auth.forms import UserCreationForm    
#from django.contrib.auth.models import User

# class BaseRegisterForm(UserCreationForm):
#     email = forms.EmailField(label = "Email")
#     first_name = forms.CharField(label = "Имя")
#     last_name = forms.CharField(label = "Фамилия")

#     class Meta:
#         model = User
#         fields = ("username", 
#                   "first_name", 
#                   "last_name", 
#                   "email", 
#                   "password1", 
#                   "password2", )    