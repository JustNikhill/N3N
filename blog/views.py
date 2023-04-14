from django.shortcuts import render, get_object_or_404

from blog.models import Article


# Create your views here.
def blogs(request):
    return render(request, 'blog.html', {'articles': Article.objects.filter(published__isnull=False)})


def article(request, slug):
    return render(request, 'article.html', {'article': get_object_or_404(Article, published__isnull=False, slug=slug)})
