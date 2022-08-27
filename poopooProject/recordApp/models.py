from django.db import models
from django.conf import settings

class Post(models.Model):
    date = models.DateTimeField(auto_now_add = True)
    hour = models.CharField()
    min = models.CharField()
    sec = models.CharField()

    def __str__(self):
        return self.date