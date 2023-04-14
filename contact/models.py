from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)