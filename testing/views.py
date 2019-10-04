from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from datetime import date
from .models import Article, User

# Create your views here.

def index(request):
    articles = Article.objects.order_by('-publication_date')[:5]
    context = {'articles': articles}
    return render(request, 'index.html', context)

def getArticle(request, articleId):
    article = get_object_or_404(Article, id=articleId)
    context = {'article': article}
    return render(request, 'article.html', context)

def createArticle(request):
    name = request.POST['publication_name']
    content = request.POST['content']
    author = get_object_or_404(User, id=1)

    article = Article(
        publication_name=name,
        content=content,
        author=author,
        publication_date=date.today()
    )

    article.save()
    return HttpResponse('successful')

def newArticle(request):
    return render(request, 'newarticle.html')
