from django.shortcuts import render
from .models import Article



def home_page(request):
    '''создаем словарь с названиями статей для применения в шаблоне'''
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request, 'home_page.html', context)
