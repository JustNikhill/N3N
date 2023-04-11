from datetime import datetime

from django.db import models

from portfolio.utils import upload_picture


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    thumbnail = models.ImageField(upload_to=upload_picture, null=True, blank=True)
    text = models.TextField(blank=True)
    writer = models.CharField(max_length=200, default='Nima')
    published = models.DateTimeField(default=datetime.now, null=True, blank=True)

    def __str__(self):
        return self.title