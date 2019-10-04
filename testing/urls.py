from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<int:articleId>/', views.getArticle, name='article'),
    path('new-article/', views.newArticle, name='new_article'),
    path('create-article/', views.createArticle, name='create_article'),
]