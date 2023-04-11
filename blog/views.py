from django.shortcuts import render

from blog.models import Article


# Create your views here.
def blogs(request):
    return render(request, 'blog.html', {'articles': Article.objects.all()})
