from django.db import models
from django.conf import settings


class Post(models.Model):
    date = models.DateTimeField(auto_now_add = True)
    hour = models.IntegerField(null=True)
    minute = models.IntegerField(null=True)
    sec = models.IntegerField(null=True)

