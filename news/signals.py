from django.db.models.signals import post_save, m2m_changed
from .models import News
from django.dispatch import receiver
from .tasks import news_out_category

@receiver(post_save, sender = News)
def notify_subscribers(sender,instance,created, **kwargs):
    if created:
        news_out_category(instance)


