from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    creation = models.DateTimeField('date created')

    def __str__(self):
        return self.username

class Article(models.Model):
    content = models.CharField(max_length=1200)
    publication_date = models.DateTimeField('date published')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_name = models.CharField(max_length=30)

    def __str__(self):
        return self.publication_name