from datetime import datetime

from django.db import models

from portfolio.utils import upload_picture


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    thumbnail = models.ImageField(upload_to=upload_picture, default="")
    text = models.TextField()
    published = models.DateTimeField(auto_now_add=datetime.now, null=True)

    def __str__(self):
        return self.title
