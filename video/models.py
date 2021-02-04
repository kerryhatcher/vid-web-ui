import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=200, default="Video Title")
    url = models.CharField(max_length=200)
    add_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    def was_added_recently(self):
        return self.add_date >= timezone.now() - datetime.timedelta(days=1)