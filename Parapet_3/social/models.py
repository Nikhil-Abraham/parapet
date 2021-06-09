from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
  body = models.TextField()
  created_on = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)


class PostArticle(models.Model):
  title = models.TextField(default='Title Goes Here ... ')
  body = models.TextField()
  created_on = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)