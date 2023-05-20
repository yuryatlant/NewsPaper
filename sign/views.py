from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm

from django.core.mail import send_mail
from datetime import datetime
from .models import BasicSignupForm
from django.shortcuts import redirect

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return render(request, 'signup.html', {})
    def post(self, request, *args, **kwargs):
        sign = BasicSignupForm(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            user_name=request.POST['user_name'],
            message=request.POST['message'],
        )
        sign.save()
         # отправляем письмо
        send_mail( 
            subject=f'{sign.user_name} {sign.date.strftime("%Y-%M-%d")}',  # имя клиента и дата записи будут в теме для удобства
            message=sign.message, # сообщение с кратким описанием проблемы
            from_email='studium2002_1@mail.ru', # здесь указываете почту, с которой будете отправлять (об этом попозже)
            recipient_list=[], # здесь список получателей. Например, секретарь, сам врач и так далее
            fail_silently = False
        )
 
        return redirect('sign:signup')

from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        premium_group.user_set.add(user)
    return redirect('/')