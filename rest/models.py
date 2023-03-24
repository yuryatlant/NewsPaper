from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone

# Create your models here.
class AbstractBaseUser(models.Model):
    password = models.CharField(('password'), max_length=128)
    last_login = models.DateTimeField(('last login'), blank=True, null=True)
    is_active = True

class AbstractUser(AbstractBaseUser):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(('username'),
        max_length=150,
        unique=True,
        help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
    first_name = models.CharField(('first name'), max_length=150, blank=True)
    last_name = models.CharField(('last name'), max_length=150, blank=True)
    email = models.EmailField(('email address'), blank=True)
    is_staff = models.BooleanField(('staff status'),
        default=False,
        help_text=('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(('active'),
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)

    
class Author(models.Model):
    raiting = models.IntegerField()
    def update_raiting(self):
        self.raiting = self.raiting*3 
        self.save()    
    author = models.OneToOneField(AbstractUser, on_delete = models.CASCADE)


class Category(models.Model):
    category_name = models.CharField(max_length = 255, unique = True)
    
class Post(models.Model):
    news = 'NW'
    article = "AR"
    POSITIONS = [
        ('NW',"новости"),('AR',"статья")]
    field = models.CharField(max_length = 10,
                             choices = POSITIONS, 
                             default = news)
    time_creation = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 30, default = "Заголовок")
    body = models.TextField(default = "Содержание")
    raiting = models.IntegerField()
    def like(self):
        self.raiting += 1
        self.save()   
    def dislike(self):
        self.raiting -= 1
        self.save() 
    def preview(self):
        return self.body[0:255] + '...'

    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    category = models.ManyToManyField(Category, through = 'PostCategory')

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(AbstractUser, on_delete = models.CASCADE)
    body = models.TextField(default = "Содержание")
    time_creation = models.DateTimeField(auto_now_add = True)
    raiting = models.IntegerField()
    def like(self):
        self.raiting += 1
        self.save()   
    def dislike(self):
        self.raiting -= 1
        self.save()  
'''
class Staff(models.Model):
    full_name = models.CharField(max_length = 255)
    
    director = 'DI'
    admin = 'AD'
    cook = 'CO'
    cashier = 'CA'
    cleaner = 'CL'

    POSITIONS = [
    (director, 'Директор'),
    (admin, 'Администратор'),
    (cook, 'Повар'),
    (cashier, 'Кассир'),
    (cleaner, 'Уборщик')]
    
    position = models.CharField(max_length = 2, 
                            choices = POSITIONS, 
                            default = cashier)
    labor_contract = models.IntegerField()

class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.FloatField(default = 0.0)
    composition = models.TextField(default = "Состав не указан")

class Order(models.Model):
    time_in = models.DateTimeField(auto_now_add = True)
    time_out = models.DateTimeField(null = True)
    cost = models.FloatField(default = 0.0)
    take_away = models.BooleanField(default = False)
    complete = models.BooleanField(default = False)
    staff = models.ForeignKey(Staff, on_delete = models.CASCADE)
    
    products = models.ManyToManyField(Product, through = 'ProductOrder')

class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    amount = models.IntegerField(default = 1) 

AbstractUser.objects.all().delete()
Author.objects.all().delete()
Post.objects.all().delete()
Category.objects.all().delete()
Comment.objects.all().delete()
PostCategory.objects.all().delete()
'''