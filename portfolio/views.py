from django.shortcuts import render

from portfolio.models import Project


def projects(request):
    return render(request, 'portfolio.html', {"projects": Project.objects.all()})