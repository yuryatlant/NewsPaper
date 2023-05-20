from django.urls import path
from .views import MailingView
#from django.contrib.auth.decorators import login_required

 
urlpatterns = [
    # path — означает путь. В данном случае путь ко всем новостям у нас останется пустым
    path('', MailingView.as_view(), name = 'mailing_page')

  ]