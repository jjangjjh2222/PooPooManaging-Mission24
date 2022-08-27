from django.db import models
from django.conf import settings

class Post(models.Model):
    date = models.DateTimeField(auto_now_add = True)
    time = models.IntegerField()

    def __str__(self):
        return self.date