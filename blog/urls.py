from django.urls import path

from blog.views import blogs

app_name = 'blog'
urlpatterns = [
    path('', blogs, name='blog'),


]
