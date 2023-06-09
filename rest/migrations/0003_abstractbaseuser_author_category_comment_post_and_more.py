# Generated by Django 4.1.7 on 2023-03-21 21:14

import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_alter_staff_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractBaseUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raiting', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(default='Содержание')),
                ('time_creation', models.DateTimeField(auto_now_add=True)),
                ('raiting', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(choices=[('news', 'новости'), ('article', 'статья')], default='news', max_length=30)),
                ('time_creation', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(default='Заголовок', max_length=30)),
                ('body', models.TextField(default='Содержание')),
                ('raiting', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.author')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.category')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.post')),
            ],
        ),
        migrations.RemoveField(
            model_name='productorder',
            name='order',
        ),
        migrations.RemoveField(
            model_name='productorder',
            name='product',
        ),
        migrations.CreateModel(
            name='AbstractUser',
            fields=[
                ('abstractbaseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rest.abstractbaseuser')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            bases=('rest.abstractbaseuser',),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductOrder',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(through='rest.PostCategory', to='rest.category'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.abstractuser'),
        ),
        migrations.AddField(
            model_name='author',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rest.abstractuser'),
        ),
    ]
