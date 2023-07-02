from django.core.management.base import BaseCommand, CommandError
from news.models import News,Category
 
 
class Command(BaseCommand):
    help = 'Подсказка команды' # показывает подсказку при вводе "python manage.py <команда> --help"
    missing_args_message = 'Недостаточно аргументов'
    requires_migrations_checks = True # напоминание о миграции

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('category', type=str)
 
    def handle(self, *args, **options):
        # здесь можете писать любой код, который выполнится при вызове вашей команды
        self.stdout.write(f"Do you really want to delete all news in {options['category']} category: yes/no") # спрашиваем пользователя, действительно ли он хочет удалить все товары
        answer =  input() # считываем подтверждение
       
        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Cancelled')) # если нет подтверждения, то отмена операции
        else:
            try:    
                # в случае подтверждения удаляем все новости в определенной категории
                categ = Category.objects.get(name=options['category'])
                News.objects.filter(category_id = categ.id).delete()
                self.stdout.write(self.style.SUCCESS(f'Succesfully wiped news in the category: {categ.name}'))
            except News.DoesNotExist:     
                self.stdout.write(self.style.ERROR(f'Could not find the category : {categ.name} ')) # нет такой категории