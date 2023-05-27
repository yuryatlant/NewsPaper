# Create your views here.
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView

from .models import BasicSignupForm
from django.shortcuts import redirect

from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

class BaseRegisterView(CreateView):
     model = User
     form_class = BasicSignupForm
     success_url = '/'
     


@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        premium_group.user_set.add(user)
    return redirect('/')


'''
from datetime import datetime
from .models import BaseRegisterForm
from django.core.mail import send_mail
from django.conf import settings

    def get(self, request, *args, **kwargs):
        return render(request, 'sign/signup.html', {})
    def post(self, request, *args, **kwargs):
        sign = BasicSignupForm(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            user_name=request.POST['user_name'],
            message=request.POST['message'],

        )
        sign.save()
         # отправляем письмо
        send_mail( 
            subject=f'{sign.user_name} {sign.date.strftime("%Y-%M-%d")}',  # имя  и дата регистрации
            message=sign.message, # сообщение с кратким описанием 
            from_email = settings.DEFAULT_FROM_EMAIL, # здесь указываете почту, с которой будете отправлять (об этом попозже)
            recipient_list=[sign.email], # здесь список получателей
            fail_silently = False
        )
 
        return redirect('sign/signup')

'''