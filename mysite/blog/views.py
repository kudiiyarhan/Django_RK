from django.shortcuts import render
from .models import Article



def home_page(request):
    '''создаем функцию возвращающую домашнюю страницу'''
    #создаем словарь с названиями статей для применения в шаблоне
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'home_page.html', context)

def article_page(request, slug):
    '''создаем функцию возвращающую страницу со статьей'''
    article = Article.objects.get(slug=slug)
    context = {'article': article}
    return render(request, 'article_page.html', context)