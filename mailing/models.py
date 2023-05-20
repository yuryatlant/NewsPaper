from django.db import models
from datetime import datetime
 
 
class Mailings(models.Model):
    date = models.DateField(
        default=datetime.utcnow,
    )
    user_name = models.CharField(
        max_length=200
    )
    message = models.TextField()
 
    def __str__(self):
        return f'{self.user_name}: {self.message}'