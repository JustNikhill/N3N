from datetime import timezone

from django.db import models

from portfolio.utils import upload_picture


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    link = models.URLField()
    thumbnail = models.ImageField(upload_to=upload_picture, default="")
    text = models.TextField()
    published = models.DateTimeField(auto_now_add=timezone.now, null=True)
