from django.template.loader import render_to_string
from django.core.mail.message import EmailMultiAlternatives
from django.conf import settings

def get_subscribers(categories):
    user_email=[]
    for user in categories.subscribers.all():
        user_email.append(user.email)
    return user_email


def news_out_category(instance):
    template ='mailing/notification1.html'
    category = instance.category
    email_subject = f'New post in category {category}'
    email_users = get_subscribers(category)
    html = render_to_string(
    template_name = template,
    context= {
        'category': category,
        'news' : instance,
        },
    )
    msg = EmailMultiAlternatives(
        subject = email_subject,
        body = '',
        from_email = settings.DEFAULT_FROM_EMAIL,
        to = email_users,
        )
    msg.attach_alternative(html, "text/html")
    msg.send()





'''        
    for category in instance.category.all():
        email_subject = f'New post in category {category}'
        email_users = get_subscribers(category)
        html = render_to_string(
            template_name = template,
            context= {
                'category': category,
                'news' : instance,
            },
        )
        msg = EmailMultiAlternatives(
            subject = email_subject,
            body = '',
            from_email = settings.DEFAULT_FROM_EMAIL,
            to = email_users,
        )
        msg.attach_alternative(html, "text/html")
        msg.send()
'''