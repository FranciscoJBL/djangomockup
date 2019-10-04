from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Article
# Create your views here.

def index(request):
    articles = Article.objects.order_by('-publication_date')[:5]
    context = {'articles': articles}
    return render(request, 'index.html', context)

def getArticle(request, articleId):
    article = get_object_or_404(Article, id=articleId)
    context = {'article': article}
    return render(request, 'article.html', context)
