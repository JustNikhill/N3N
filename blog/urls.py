from django.urls import path

from blog.views import blogs, article

app_name = 'blog'
urlpatterns = [
    path('', blogs, name='blog'),
    path('<slug>/', article, name='article'),

]
