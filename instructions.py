python3 manage.py shell
from rest.models import AbstractUser
from rest.models import Author
from rest.models import Post
from rest.models import Category
from rest.models import Comment
from rest.models import PostCategory
user1 = AbstractUser.objects.create(username = "Виктор Сухоруков")
user2 = AbstractUser.objects.create(username = "Данила Богров")
author1 = Author.objects.create(raiting = 2, author = user1)
author2 = Author.objects.create(raiting = 5, author = user2)
category1 = Category.objects.create(category_name = "Спорт")                              
category2 = Category.objects.create(category_name = "Политика")  
category3 = Category.objects.create(category_name = "Образование")  
category4 = Category.objects.create(category_name = "Экономика")  
post1 = Post.objects.create(field = Post.article, title = "Статья №1", body = "текст первой статьи",raiting = 1, author = author1)  
post2 = Post.objects.create(field = Post.article, title = "Статья №2", body = "текст второй статьи",raiting = 2, author = author2) 
post3 = Post.objects.create(field = Post.news, title = "Чудесные новости", body = "Открыли БКЛ",raiting = 5, author = author1)
сonnect1 = PostCategory.objects.create(post = post1, category = category2)
сonnect2 = PostCategory.objects.create(post = post1, category = category4)
сonnect3 = PostCategory.objects.create(post = post2, category = category3)
сonnect4 = PostCategory.objects.create(post = post2, category = category1)
сonnect5 = PostCategory.objects.create(post = post3, category = category4)
comment1 = Comment.objects.create(post = post1, user = user1, body = "комментарий от 1-го пользователя", raiting = 1)
comment2 = Comment.objects.create(post = post1, user = user2, body = "комментарий от 2-го пользователя", raiting = 3)
comment3 = Comment.objects.create(post = post2, user = user1, body = "очень умные мысли", raiting = 0)
comment4 = Comment.objects.create(post = post3, user = user2, body = "улет", raiting = 5)
post1.like()
post2.like()
post3.dislike()
comment1.like()
comment2.dislike()
comment3.like()
comment4.dislike()
author1.update_raiting()
author2.update_raiting()
AbstractUser.objects.all().order_by('-author__raiting').values('username','author__raiting')[0]
Comment.objects.all().order_by('-raiting').values('post__time_creation', 'user__username', 'post__raiting', 'post__title')[0]
