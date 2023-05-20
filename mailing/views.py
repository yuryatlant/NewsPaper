from django.shortcuts import render, reverse, redirect
from django.views import View

from datetime import datetime

from .models import Mailings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives # импортируем класс для создание объекта письма с html
from django.template.loader import render_to_string # импортируем функцию, которая срендерит наш html в текст

class MailingView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mailing/make_mailing.html', {})
 
    def post(self, request, *args, **kwargs):
        mailing = Mailings(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            user_name=request.POST['user_name'],
            message=request.POST['message'],
        )
        mailing.save()
        # отправляем письмо
        #send_mail( 
        #    subject=f'{mailing.user_name} {mailing.date.strftime("%Y-%M-%d")}',  # имя клиента и дата записи будут в теме для удобства
        #    message=mailing.message, # сообщение с кратким описанием проблемы
        #    from_email='studium2002_1@mail.ru', # здесь указываете почту, с которой будете отправлять (об этом попозже)
        #    recipient_list=['studium2002@mail.ru'] # здесь список получателей. Например, секретарь, сам врач и так далее
        #)
        html_content = render_to_string( 
            'mailing/mail_created.html',
            {'mailes': mailing })
        # в конструкторе уже знакомые нам параметры, да? Называются правда немного по другому, но суть та же.
        msg = EmailMultiAlternatives(
            subject=f'{mailing.user_name} {mailing.date.strftime("%Y-%M-%d")}',
            body=mailing.message, #  это то же, что и message
            from_email='studium2002_1@mail.ru',
            to=['studium2002@mail.ru'], # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html") # добавляем html

        msg.send() # отсылаем

        return redirect('mailing_page')