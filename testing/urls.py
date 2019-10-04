from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<int:articleId>/', views.getArticle, name='article'),
]