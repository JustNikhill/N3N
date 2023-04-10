from django.urls import path

from portfolio.views import projects

app_name = 'portfolio'
urlpatterns = [
    path('', projects, name='project')
]