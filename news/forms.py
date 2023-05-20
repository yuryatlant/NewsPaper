from django.forms import ModelForm
from .models import News
 
# Создаём модельную форму
class NewsForm(ModelForm):
    # модель, по которой будет строиться форма и нужные нам поля. 
    class Meta:
        model = News
        fields = ['name', 'description', 'category']



