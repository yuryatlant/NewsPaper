# Generated by Django 4.1.7 on 2023-03-23 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0003_abstractbaseuser_author_category_comment_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='field',
            field=models.CharField(choices=[('NW', 'новости'), ('AR', 'статья')], default='NW', max_length=10),
        ),
    ]