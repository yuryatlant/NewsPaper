from django_filters import FilterSet # импортируем filterset
from .models import News
 
 
# создаём фильтр
class NewsFilter(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т.е. подбираться) информация о новостях
    class Meta:
        model = News
        fields = {
            'name': ['icontains'], # чтобы нам выводило имя хотя бы отдалённо похожее на то, что запросил пользователь
            'category' : ['exact'],
            'time_creation' : ['gt']
        }